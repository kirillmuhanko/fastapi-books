from pydantic import BaseModel


class UserLoginServiceDto(BaseModel):
    username: str
    password: str
