from typing import Optional, Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.books_db_context.user_model import UserModel
from app.db.repositories.base_repository import BaseRepository
from app.user.mappings.user_model_mappings import map_user_model_to_user_model


class UserRepository(BaseRepository[UserModel]):
    def __init__(self, db: AsyncSession):
        super().__init__(db)

    async def create(self, user: UserModel) -> UserModel:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

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

    async def update(self, user_id: UUID, updated_user: UserModel) -> Optional[UserModel]:
        existing_user = await self.get(user_id)
        if not existing_user:
            return None
        existing_user = map_user_model_to_user_model(existing_user, updated_user)
        await self.db.commit()
        await self.db.refresh(existing_user)
        return existing_user

    async def delete(self, user_id: UUID) -> bool:
        user = await self.get(user_id)
        if user:
            await self.db.delete(user)
            await self.db.commit()
            return True
        return False

    async def bulk_create(self, users: Sequence[UserModel]) -> Sequence[UserModel]:
        try:
            async with self.db.begin():
                self.db.add_all(users)
            await self.db.commit()
            for user in users:
                await self.db.refresh(user)
            return users
        except SQLAlchemyError as e:
            await self.db.rollback()
            raise e

    async def bulk_update(self, updated_users: Sequence[UserModel]) -> Sequence[UserModel]:
        try:
            user_ids = [user.id for user in updated_users]
            result = await self.db.execute(select(UserModel).filter(UserModel.id.in_(user_ids)))
            existing_users = result.scalars().all()
            existing_users_dict = {user.id: user for user in existing_users}
            updated_list = []
            for updated_user in updated_users:
                existing_user = existing_users_dict.get(updated_user.id)
                if existing_user:
                    mapped_user = map_user_model_to_user_model(existing_user, updated_user)
                    updated_list.append(mapped_user)
            await self.db.commit()
            for user in updated_list:
                await self.db.refresh(user)
            return updated_list

        except SQLAlchemyError as e:
            await self.db.rollback()
            raise e

    async def bulk_delete(self, user_ids: Sequence[UUID]) -> int:
        try:
            async with self.db.begin():
                result = await self.db.execute(
                    select(UserModel).filter(UserModel.id.in_(user_ids))
                )
                users_to_delete = result.scalars().all()
                for user in users_to_delete:
                    await self.db.delete(user)
            await self.db.commit()
            return len(users_to_delete)
        except SQLAlchemyError as e:
            await self.db.rollback()
            raise e
