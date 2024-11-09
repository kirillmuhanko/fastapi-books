from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from app.controllers_dtos.auth.user_login_request_dto import UserLoginRequestDto
from app.controllers_dtos.auth.user_register_request_dto import UserRegisterRequestDto
from app.dependency_injection.service_registry import get_auth_service
from app.models.auth.auth_token_model import AuthTokenModel
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user_register_request_dto: UserRegisterRequestDto,
                   auth_service: AuthService = Depends(get_auth_service)):
    user_register_service_dto = user_register_request_dto.to_service_dto()
    await auth_service.create_user(user_register_service_dto)


@router.post("/login", response_model=AuthTokenModel)
async def login(user_login_request_dto: Annotated[UserLoginRequestDto, Depends()],
                auth_service: AuthService = Depends(get_auth_service)):
    user_login_service_dto = user_login_request_dto.to_service_dto()
    await auth_service.authenticate_user(user_login_service_dto)
