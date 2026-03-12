import enum
import uuid
from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, Text, JSON, Uuid
from sqlalchemy.orm import relationship

from app.db.session import Base

class TransactionStatus(str, enum.Enum):
    PENDING = "PENDING"
    FUNDED = "FUNDED"
    COMPLETED = "COMPLETED"
    DISPUTED = "DISPUTED"
    RELEASED = "RELEASED"

class EscrowTransaction(Base):
    __tablename__ = "escrow_transactions"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    buyer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(Enum(TransactionStatus), default=TransactionStatus.PENDING, nullable=False)
    conditions = Column(JSON, nullable=True) # Array of strings
    submission_text = Column(Text, nullable=True)
    ai_score = Column(Integer, nullable=True)
    ai_verdict = Column(Text, nullable=True)

    buyer = relationship("User", foreign_keys=[buyer_id])
    seller = relationship("User", foreign_keys=[seller_id])
