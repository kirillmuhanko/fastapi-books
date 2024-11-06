from repositories.user_repository import UserRepository
from fastapi import Depends
from dependencies.repository_dependencies import get_user_repository

class UserService:
    def __init__(self, user_repository: UserRepository = Depends(get_user_repository)):
        self.user_repository = user_repository

    async def get_user(self, user_id: int):
        user = await self.user_repository.get_user(user_id)
        return user
