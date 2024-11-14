from app.db.models.books_db_context.user_model import UserModel


def map_user_model(existing_user: UserModel, new_user_data: UserModel) -> UserModel:
    existing_user.email = new_user_data.email
    existing_user.username = new_user_data.username
    existing_user.first_name = new_user_data.first_name
    existing_user.last_name = new_user_data.last_name
    existing_user.hashed_password = new_user_data.hashed_password
    existing_user.is_active = new_user_data.is_active
    existing_user.role = new_user_data.role
    existing_user.phone_number = new_user_data.phone_number
    return existing_user
