from abc import ABC, abstractmethod
from typing import TypeVar, Any, Generic, Optional, Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

_T = TypeVar("_T", bound=Any)


class BaseRepository(ABC, Generic[_T]):
    def __init__(self, db: AsyncSession):
        self.db = db

    @abstractmethod
    async def create(self, entity: _T):
        pass

    @abstractmethod
    async def get(self, entity_id: UUID) -> Optional[_T]:
        pass

    @abstractmethod
    async def get_all(self, limit: int = 100, offset: int = 0) -> Sequence[_T]:
        pass

    @abstractmethod
    async def update(self, entity: _T) -> Optional[_T]:
        pass

    @abstractmethod
    async def delete(self, entity_id: UUID) -> None:
        pass

    @abstractmethod
    async def bulk_create(self, entities: Sequence[_T]) -> Sequence[_T]:
        pass

    @abstractmethod
    async def bulk_update(self, entities: Sequence[_T]) -> Sequence[_T]:
        pass

    @abstractmethod
    async def bulk_delete(self, entity_ids: Sequence[UUID]) -> None:
        pass

    async def begin_transaction(self):
        await self.db.begin()

    async def rollback_transaction(self):
        await self.db.rollback()

    async def commit(self) -> None:
        await self.db.commit()

    async def refresh(self, entity: _T) -> None:
        await self.db.refresh(entity)

    async def refresh_bulk(self, entities: Sequence[_T]) -> None:
        for entity in entities:
            await self.db.refresh(entity)
