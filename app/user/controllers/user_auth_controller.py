from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from app.user.dependencies import get_auth_service
from app.user.dtos.user_auth_dtos import UserRegisterDto, UserLoginDto
from app.user.dtos.user_auth_request_dtos import UserRegisterRequestDto
from app.user.models.user_auth_models import AuthTokenModel
from app.user.services.user_auth_service import UserAuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user_register_request_dto: UserRegisterRequestDto,
                   auth_service: UserAuthService = Depends(get_auth_service)):
    user_register_dto = UserRegisterDto.model_validate(user_register_request_dto)
    await auth_service.create_user(user_register_dto)


@router.post("/login", response_model=AuthTokenModel)
async def login(oauth2_password_request_form: Annotated[OAuth2PasswordRequestForm, Depends()],
                auth_service: UserAuthService = Depends(get_auth_service)):
    user_login_dto = UserLoginDto.model_validate(oauth2_password_request_form)
    access_token = await auth_service.authenticate_user(user_login_dto)
    return AuthTokenModel(access_token=access_token, token_type="Bearer")
