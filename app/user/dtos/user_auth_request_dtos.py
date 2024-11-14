from pydantic import BaseModel, EmailStr, Field


class UserRegisterRequestDto(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    username: str = Field(..., min_length=3, max_length=20, description="User's username")
    first_name: str = Field(..., min_length=2, max_length=50, description="User's first name")
    last_name: str = Field(..., min_length=2, max_length=50, description="User's last name")
    password: str = Field(..., min_length=8, max_length=128, description="User's password")
    role: str = Field(..., description="User's role")

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
