from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class UserInDBBase(UserBase):
    id: int
    wallet_balance: float

    model_config = ConfigDict(from_attributes=True)

class User(UserInDBBase):
    pass
