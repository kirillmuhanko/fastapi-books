from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from app.controllers_dtos.auth.user_register_request_dto import UserRegisterRequestDto
from app.dependency_injection.service_registry import get_auth_service
from app.models.auth.auth_token_model import AuthTokenModel
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user_register_request: UserRegisterRequestDto,
                   auth_service: AuthService = Depends(get_auth_service)):
    user_register_service_dto = user_register_request.to_service_dto()
    await auth_service.register_user(user_register_service_dto)
    pass


@router.post("/login", response_model=AuthTokenModel)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return {"access_token": "123", "token_type": "bearer"}
