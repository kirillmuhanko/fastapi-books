from fastapi import Depends

from app.dependency_injection.repository_registry import get_user_repository
from app.dependency_injection.security_util_registry import get_password_hasher
from app.repositories.user_repository import UserRepository
from app.security_utils.password_hasher import PasswordHasher
from app.services_dtos.auth.user_register_service_dto import UserRegisterServiceDto


class AuthService:
    def __init__(self,
                 user_repository: UserRepository = Depends(get_user_repository),
                 password_hasher: PasswordHasher = Depends(get_password_hasher)):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    async def register_user(self, user: UserRegisterServiceDto):
        hashed_password = self.password_hasher.hash_password(user.password)
        pass
