from pydantic import BaseModel


class UserRegisterResponseDto(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool
