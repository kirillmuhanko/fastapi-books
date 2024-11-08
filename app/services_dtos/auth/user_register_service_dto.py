from pydantic import BaseModel


class UserRegisterServiceDto(BaseModel):
    id: int
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    role: str
