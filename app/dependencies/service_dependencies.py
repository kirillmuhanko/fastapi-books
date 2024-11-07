from app.services.user_service import UserService


async def get_user_service() -> UserService:
    return UserService()
