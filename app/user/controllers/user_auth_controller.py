from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from app.user.dependencies import get_auth_service
from app.user.dtos.user_auth_request_dtos import UserLoginRequestDto, UserRegisterRequestDto
from app.user.models.user_auth_models import AuthTokenModel
from app.user.services.user_auth_service import UserAuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user_register_request_dto: UserRegisterRequestDto,
                   auth_service: UserAuthService = Depends(get_auth_service)):
    user_register_service_dto = user_register_request_dto.to_service_dto()
    await auth_service.create_user(user_register_service_dto)


@router.post("/login", response_model=AuthTokenModel)
async def login(user_login_request_dto: Annotated[UserLoginRequestDto, Depends()],
                auth_service: UserAuthService = Depends(get_auth_service)):
    user_login_service_dto = user_login_request_dto.to_service_dto()
    access_token = await auth_service.authenticate_user(user_login_service_dto)
    return AuthTokenModel(access_token=access_token, token_type="Bearer")
