from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class EscrowTransactionBase(BaseModel):
    buyer_id: int
    seller_id: int
    amount: float
    description: str

class EscrowTransactionCreate(EscrowTransactionBase):
    pass

class EscrowTransactionInDBBase(EscrowTransactionBase):
    id: int
    status: str
    conditions: str
    ai_score: Optional[float] = None
    ai_verdict: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EscrowTransaction(EscrowTransactionInDBBase):
    pass

class AgreementRequest(BaseModel):
    description: str

class AgreementResponse(BaseModel):
    conditions: str

class VerificationRequest(BaseModel):
    escrow_id: int
    submission: str

class VerificationResponse(BaseModel):
    ai_score: float
    ai_verdict: str
    status: str
