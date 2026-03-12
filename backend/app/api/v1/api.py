from fastapi import APIRouter
from app.api.v1.endpoints import user, escrow

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(escrow.router, prefix="/escrows", tags=["escrows"])
