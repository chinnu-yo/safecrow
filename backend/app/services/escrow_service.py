from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.escrow import EscrowTransaction
from app.models.user import User
from app.schemas.escrow import EscrowTransactionCreate
from app.services.ai_service import ai_service
from app.core.exceptions import DatabaseError, ValidationError

class EscrowService:
    async def create_escrow(
        self, db: AsyncSession, escrow_in: EscrowTransactionCreate
    ) -> EscrowTransaction:
        """
        Create a new escrow transaction, automatically generating conditions 
        from the provided description via AI.
        """
        # Generate conditions
        conditions = ai_service.generate_conditions(escrow_in.description)
        
        escrow = EscrowTransaction(
            buyer_id=escrow_in.buyer_id,
            seller_id=escrow_in.seller_id,
            amount=escrow_in.amount,
            description=escrow_in.description,
            conditions=conditions,
            status="CREATED"
        )
        db.add(escrow)
        try:
            await db.commit()
            await db.refresh(escrow)
        except Exception as e:
            await db.rollback()
            raise DatabaseError("Failed to create escrow transaction") from e
        return escrow

    async def fund_escrow(
        self, db: AsyncSession, escrow_id: int
    ) -> Optional[EscrowTransaction]:
        """
        Fund an escrow. In a real app, this would involve Stripe/Crypto.
        For now, we deduct from buyer's internal wallet balance and update status.
        """
        result = await db.execute(select(EscrowTransaction).where(EscrowTransaction.id == escrow_id))
        escrow = result.scalar_one_or_none()
        
        if not escrow or escrow.status != "CREATED":
            return None
            
        # Get buyer
        user_result = await db.execute(select(User).where(User.id == escrow.buyer_id))
        buyer = user_result.scalar_one_or_none()
        
        if not buyer or buyer.wallet_balance < escrow.amount:
            raise ValidationError("Insufficient funds or buyer not found")
            
        # Deduct funds (simulated funding)
        buyer.wallet_balance -= escrow.amount
        escrow.status = "FUNDED"
        
        try:
            await db.commit()
            await db.refresh(escrow)
        except Exception as e:
            await db.rollback()
            raise DatabaseError("Failed to fund escrow transaction") from e
        return escrow

    async def get_escrow(self, db: AsyncSession, escrow_id: int) -> Optional[EscrowTransaction]:
        result = await db.execute(select(EscrowTransaction).where(EscrowTransaction.id == escrow_id))
        return result.scalar_one_or_none()

    async def verify_submission(
        self, db: AsyncSession, escrow_id: int, submission: str
    ) -> Optional[EscrowTransaction]:
        """
        Verify the seller's submission against the escrow conditions using AI.
        If the score is high enough (e.g., >= 0.8), release the funds.
        """
        escrow = await self.get_escrow(db, escrow_id)
        if not escrow or escrow.status != "FUNDED":
            return None
            
        verification_result = ai_service.verify_submission(escrow.conditions, submission)
        escrow.ai_score = verification_result["ai_score"]
        escrow.ai_verdict = verification_result["ai_verdict"]
        
        # Threshold for automatic completion
        if escrow.ai_score >= 0.8:
            escrow.status = "COMPLETED"
            # In a real system, we'd add to the seller's wallet here
            user_result = await db.execute(select(User).where(User.id == escrow.seller_id))
            seller = user_result.scalar_one_or_none()
            if seller:
                seller.wallet_balance += escrow.amount
        else:
            escrow.status = "DISPUTED" # or keep FUNDED and ask for iteration
            
        try:
            await db.commit()
            await db.refresh(escrow)
        except Exception as e:
            await db.rollback()
            raise DatabaseError("Failed to update escrow transaction upon verification") from e
            
        return escrow

escrow_service = EscrowService()
