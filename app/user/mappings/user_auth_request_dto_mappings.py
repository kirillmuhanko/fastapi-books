from fastapi.security import OAuth2PasswordRequestForm

from app.user.dtos.user_auth_dtos import UserRegisterDto, UserLoginDto
from app.user.dtos.user_auth_request_dtos import UserRegisterRequestDto


def map_user_register_request_dto_to_user_register_dto(request_dto: UserRegisterRequestDto) -> UserRegisterDto:
    return UserRegisterDto(
        email=request_dto.email,
        username=request_dto.username,
        first_name=request_dto.first_name,
        last_name=request_dto.last_name,
        password=request_dto.password,
        role=request_dto.role
    )


def map_oauth2_password_request_form_to_user_login_dto(request_form: OAuth2PasswordRequestForm):
    return UserLoginDto(
        username=request_form.username,
        password=request_form.password
    )
