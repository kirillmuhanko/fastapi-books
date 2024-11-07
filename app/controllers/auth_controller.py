from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from starlette import status
from app.controllers_dtos.auth.user_register_request_dto import UserRegisterRequestDto
from app.dependencies.service_dependencies import get_user_service
from app.services.user_service import UserService
from app.models.database.user_model import UserModel
from app.core.database import get_db
from pydantic import BaseModel, Field
from typing import Optional

from app.repositories.user_repository import UserRepository

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user_register_request: UserRegisterRequestDto):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


@router.post("/login", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return {"access_token": "123", "token_type": "bearer"}

UserRepository