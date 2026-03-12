from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.api.dependencies import get_db
from app.models.user import User
from app.schemas.user import User as UserSchema, UserCreate
from app.core.exceptions import DatabaseError

router = APIRouter()

@router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    try:
        user = User(username=user_in.username, wallet_balance=0.0)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Database Error: " + str(e))

@router.get("/{user_id}", response_model=UserSchema)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
