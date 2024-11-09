from fastapi.security import OAuth2PasswordRequestForm

from app.services_dtos.auth.user_login_service_dto import UserLoginServiceDto


class UserLoginRequestDto(OAuth2PasswordRequestForm):
    def to_service_dto(self):
        return UserLoginServiceDto(
            username=self.username,
            password=self.password
        )
