from typing import Optional, List
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.books_db_context.user_model import UserModel
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[UserModel]):
    def __init__(self, db: Session):
        super().__init__(db)

    async def create(self, user: UserModel) -> None:
        self.db.add(user)

    async def get(self, user_id: UUID) -> Optional[UserModel]:
        user = self.db.query(UserModel).filter_by(id=user_id).first()
        return user

    async def get_by_username(self, username: str) -> Optional[UserModel]:
        user = self.db.query(UserModel).filter_by(username=username).first()
        return user

    async def get_all(self, limit: int = 100, offset: int = 0) -> List[UserModel]:
        users = self.db.query(UserModel).offset(offset).limit(limit).all()
        return users

    async def update(self, user: UserModel) -> Optional[UserModel]:
        existing_user = await self.get(user.id)
        if existing_user:
            existing_user.email = user.email
            existing_user.username = user.username
            existing_user.first_name = user.first_name
            existing_user.last_name = user.last_name
            existing_user.hashed_password = user.hashed_password
            existing_user.is_active = user.is_active
            existing_user.role = user.role
            existing_user.phone_number = user.phone_number
            return existing_user
        return None

    async def delete(self, user_id: UUID) -> None:
        user = await self.get(user_id)
        if user:
            self.db.delete(user)

    async def bulk_create(self, users: List[UserModel]) -> List[UserModel]:
        self.db.add_all(users)
        return users

    async def bulk_update(self, users: List[UserModel]) -> List[UserModel]:
        for user in users:
            existing_user = await self.get(user.id)
            if existing_user:
                existing_user.email = user.email
                existing_user.username = user.username
                existing_user.first_name = user.first_name
                existing_user.last_name = user.last_name
                existing_user.hashed_password = user.hashed_password
                existing_user.is_active = user.is_active
                existing_user.role = user.role
                existing_user.phone_number = user.phone_number
        return users

    async def bulk_delete(self, user_ids: List[UUID]) -> None:
        users = self.db.query(UserModel).filter(UserModel.id.in_(user_ids)).all()
        for user in users:
            self.db.delete(user)
