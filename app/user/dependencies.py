from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.user.repositories.user_repository import UserRepository
from app.user.services.user_auth_service import UserAuthService


def get_user_repository(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_auth_service(user_repository: UserRepository = Depends(get_user_repository)) -> UserAuthService:
    return UserAuthService(user_repository)
