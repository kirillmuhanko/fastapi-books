from pydantic import BaseModel

from app.db.models.books_db_context.user_model import UserModel


class UserRegisterDto(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    role: str

    def to_model(self, hashed_password: str) -> UserModel:
        """Maps the DTO to a User Model instance."""
        return UserModel(
            email=self.email,
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            hashed_password=hashed_password,
            role=self.role
        )


class UserLoginDto(BaseModel):
    username: str
    password: str
