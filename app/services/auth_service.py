from app.repositories.user_repository import UserRepository
from app.security_utils.password_hasher import PasswordHasher
from app.services_dtos.auth.user_register_service_dto import UserRegisterServiceDto


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def register_user(self, user_dto: UserRegisterServiceDto):
        hashed_password = PasswordHasher.hash_password(user_dto.password)
        user_model = user_dto.to_model(hashed_password)
        new_user = await self.user_repository.create_user(user_model)
