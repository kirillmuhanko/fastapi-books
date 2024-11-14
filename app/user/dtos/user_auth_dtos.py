from pydantic import BaseModel


class UserRegisterDto(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    role: str


class UserLoginDto(BaseModel):
    username: str
    password: str
