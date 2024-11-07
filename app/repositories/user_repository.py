from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.database.user_model import UserModel
import logging
from fastapi import Depends

class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    async def get_user(self, user_id: int):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info(f"Initialized UserRepository with session ID: {id(self.db)}")
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        return user
