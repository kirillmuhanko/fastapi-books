from app.db.models.books_db_context.user_model import UserModel
from app.user.dtos.user_auth_dtos import UserRegisterDto


def map_user_register_dto_to_user_model(user_register_dto: UserRegisterDto, hashed_password: str) -> UserModel:
    return UserModel(
        email=user_register_dto.email,
        username=user_register_dto.username,
        first_name=user_register_dto.first_name,
        last_name=user_register_dto.last_name,
        hashed_password=hashed_password,
        role=user_register_dto.role
    )
