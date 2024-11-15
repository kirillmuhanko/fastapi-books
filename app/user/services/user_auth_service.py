from datetime import timedelta

from fastapi import HTTPException
from starlette import status

from app.core.config import settings
from app.security.generators.token_generator import TokenGenerator
from app.security.hashers.password_hasher import PasswordHasher
from app.user.dtos.user_auth_dtos import UserRegisterDto, UserLoginDto
from app.user.mappings.user_auth_dto_mappings import map_user_register_dto_to_user_model
from app.user.repositories.user_repository import UserRepository


class UserAuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, new_user_dto: UserRegisterDto):
        hashed_password = PasswordHasher.hash_password(new_user_dto.password)
        user_model = map_user_register_dto_to_user_model(new_user_dto, hashed_password)
        await self.user_repository.create(user_model)

    async def authenticate_user(self, login_dto: UserLoginDto):
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
            timedelta(weeks=settings.access_token_expire_weeks))

        return token
