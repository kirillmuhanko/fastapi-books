from pydantic import BaseModel, EmailStr, Field
from pydantic_settings import SettingsConfigDict


class UserRegisterRequestDto(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    username: str = Field(..., min_length=3, max_length=20, description="User's username")
    first_name: str = Field(..., min_length=2, max_length=50, description="User's first name")
    last_name: str = Field(..., min_length=2, max_length=50, description="User's last name")
    password: str = Field(..., min_length=8, max_length=128, description="User's password")
    role: str = Field(..., description="User's role")

    model_config = SettingsConfigDict(
        json_schema_extra={
            "example": {
                "email": "test@example.com",
                "username": "test_user",
                "first_name": "Test",
                "last_name": "User",
                "password": "Test1234",
                "role": "test_role"
            }
        }
    )
