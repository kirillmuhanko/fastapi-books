from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, Field

from app.user.dtos.user_auth_dtos import UserRegisterDto, UserLoginDto


class UserRegisterRequestDto(BaseModel):
    """
    DTO for user registration.
    """
    email: EmailStr = Field(..., description="User's email address")
    username: str = Field(..., min_length=3, max_length=20, description="User's username")
    first_name: str = Field(..., min_length=2, max_length=50, description="User's first name")
    last_name: str = Field(..., min_length=2, max_length=50, description="User's last name")
    password: str = Field(..., min_length=8, max_length=128, description="User's password")
    role: str = Field(..., description="User's role")

    def to_service_dto(self) -> UserRegisterDto:
        """Converts to service DTO."""
        return UserRegisterDto(
            email=self.email,
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            password=self.password,
            role=self.role
        )

    class Config:
        json_schema_extra = {
            "example": {
                "email": "john.doe@example.com",
                "username": "johndoe123",
                "first_name": "John",
                "last_name": "Doe",
                "password": "StrongPassword123!",
                "role": "user"
            }
        }


class UserLoginRequestDto(OAuth2PasswordRequestForm):
    def to_service_dto(self):
        return UserLoginDto(
            username=self.username,
            password=self.password
        )
