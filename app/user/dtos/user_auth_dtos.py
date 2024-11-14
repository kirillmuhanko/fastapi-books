from pydantic import BaseModel


class UserRegisterDto(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    role: str

    model_config = {
        'from_attributes': True
    }


class UserLoginDto(BaseModel):
    username: str
    password: str

    model_config = {
        'from_attributes': True
    }
