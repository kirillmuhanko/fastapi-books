from typing import Optional, Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.books_db_context.user_model import UserModel
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[UserModel]):
    def __init__(self, db: AsyncSession):
        super().__init__(db)

    async def create(self, user: UserModel) -> None:
        self.db.add(user)

    async def get(self, user_id: UUID) -> Optional[UserModel]:
        result = await self.db.execute(select(UserModel).filter_by(id=user_id))
        user = result.scalar_one_or_none()
        return user

    async def get_by_username(self, username: str) -> Optional[UserModel]:
        result = await self.db.execute(select(UserModel).filter_by(username=username))
        user = result.scalar_one_or_none()
        return user

    async def get_all(self, limit: int = 100, offset: int = 0) -> Sequence[UserModel]:
        result = await self.db.execute(
            select(UserModel).offset(offset).limit(limit)
        )
        users = result.scalars().all()
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
            await self.db.delete(user)
            await self.db.commit()

    async def bulk_create(self, users: Sequence[UserModel]) -> Sequence[UserModel]:
        self.db.add_all(users)
        return users

    async def bulk_update(self, users: Sequence[UserModel]) -> Sequence[UserModel]:
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

    async def bulk_delete(self, user_ids: Sequence[UUID]) -> None:
        result = await self.db.execute(
            select(UserModel).filter(UserModel.id.in_(user_ids))
        )
        users = result.scalars().all()
        for user in users:
            await self.db.delete(user)
        await self.db.commit()
