from app.security_utils.password_hasher import PasswordHasher
from app.security_utils.token_generator import TokenGenerator


async def get_password_hasher() -> PasswordHasher:
    return PasswordHasher()


async def get_token_generator() -> TokenGenerator:
    return TokenGenerator()
