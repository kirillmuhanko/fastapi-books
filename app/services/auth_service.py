from datetime import timedelta

from fastapi import HTTPException
from starlette import status

from app.repositories.user_repository import UserRepository
from app.security_utils.password_hasher import PasswordHasher
from app.security_utils.token_generator import TokenGenerator
from app.services_dtos.auth.user_login_service_dto import UserLoginServiceDto
from app.services_dtos.auth.user_register_service_dto import UserRegisterServiceDto


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, new_user_dto: UserRegisterServiceDto):
        hashed_password = PasswordHasher.hash_password(new_user_dto.password)
        user_model = new_user_dto.to_model(hashed_password)
        await self.user_repository.create(user_model)
        await self.user_repository.commit()

    async def authenticate_user(self, login_dto: UserLoginServiceDto):
        existing_user = await self.user_repository.get_by_username(login_dto.username)
        password_is_valid = PasswordHasher.verify_password(login_dto.password, existing_user.hashed_password)

        if not password_is_valid:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Invalid credentials.')

        user_uuid_str = str(existing_user.id)

        token = TokenGenerator.create_access_token(
            existing_user.username,
            user_uuid_str,
            existing_user.role,
            timedelta(weeks=4))

        return token
