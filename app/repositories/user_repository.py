import logging

from sqlalchemy.orm import Session

from app.models.books_db_context.user_model import UserModel


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create_user(self, user: UserModel):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    async def get_by_username(self, username: str):
        user = self.db.query(UserModel).filter_by(username=username).first()
        return user

    async def get_user(self, user_id: int):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info(f"Initialized UserRepository with session ID: {id(self.db)}")
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        return user
