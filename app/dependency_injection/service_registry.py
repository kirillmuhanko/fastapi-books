from app.services.auth_service import AuthService
from app.services.user_service import UserService


async def get_auth_service() -> AuthService:
    return AuthService()


async def get_user_service() -> UserService:
    return UserService()
