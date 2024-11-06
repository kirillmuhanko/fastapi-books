from pydantic import BaseModel


class UserRegisterRequestDto(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

# make hashed_password field for service layer, it will be mapped manually.