from pydantic import BaseModel


class AuthTokenModel(BaseModel):
    access_token: str
    token_type: str
