from fastapi import APIRouter, Depends
from app.dependencies import get_current_active_user
from app.models import User


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/me', tags=['users'])
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
