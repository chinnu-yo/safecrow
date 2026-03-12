from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.api.dependencies import get_db
from app.schemas.escrow import (
    EscrowTransaction, 
    EscrowTransactionCreate, 
    VerificationRequest
)
from app.services.escrow_service import escrow_service
from app.core.exceptions import ValidationError, DatabaseError

router = APIRouter()

@router.post("/", response_model=EscrowTransaction, status_code=status.HTTP_201_CREATED)
async def create_escrow(
    escrow_in: EscrowTransactionCreate,
    db: AsyncSession = Depends(get_db)
):
    try:
        return await escrow_service.create_escrow(db, escrow_in)
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{escrow_id}", response_model=EscrowTransaction)
async def get_escrow(
    escrow_id: int,
    db: AsyncSession = Depends(get_db)
):
    escrow = await escrow_service.get_escrow(db, escrow_id)
    if not escrow:
        raise HTTPException(status_code=404, detail="Escrow Transaction not found")
    return escrow

@router.post("/{escrow_id}/fund", response_model=EscrowTransaction)
async def fund_escrow(
    escrow_id: int,
    db: AsyncSession = Depends(get_db)
):
    try:
        escrow = await escrow_service.fund_escrow(db, escrow_id)
        if not escrow:
            raise HTTPException(status_code=404, detail="Escrow Transaction not found or already funded")
        return escrow
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/{escrow_id}/verify", response_model=EscrowTransaction)
async def verify_escrow(
    escrow_id: int,
    verify_in: VerificationRequest,
    db: AsyncSession = Depends(get_db)
):
    if escrow_id != verify_in.escrow_id:
        raise HTTPException(status_code=400, detail="Escrow ID mismatch")
        
    try:
        escrow = await escrow_service.verify_submission(db, escrow_id, verify_in.submission)
        if not escrow:
            raise HTTPException(status_code=404, detail="Escrow Transaction not found or not in FUNDED state")
        return escrow
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
