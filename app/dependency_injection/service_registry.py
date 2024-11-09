from fastapi import Depends

from app.dependency_injection.repository_registry import get_user_repository
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.user_service import UserService


def get_auth_service(user_repository: UserRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(user_repository)


async def get_user_service() -> UserService:
    return UserService()
