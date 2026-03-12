from sqlalchemy import Column, Integer, String, Float

from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    wallet_balance = Column(Float, default=1000.0, nullable=False)
