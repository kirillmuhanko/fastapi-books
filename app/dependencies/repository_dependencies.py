from repositories.user_repository import UserRepository


async def get_user_repository() -> UserRepository:
    return UserRepository()
