from abc import ABC, abstractmethod
from typing import TypeVar, Any, Generic, Optional, Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

_T = TypeVar("_T", bound=Any)


class BaseRepository(ABC, Generic[_T]):
    def __init__(self, db: AsyncSession):
        """
        Initialize the repository with a database session.
        """
        self.db = db

    @abstractmethod
    async def create(self, entity: _T) -> _T:
        pass

    @abstractmethod
    async def get(self, entity_id: UUID) -> Optional[_T]:
        pass

    @abstractmethod
    async def get_all(self, limit: int = 100, offset: int = 0) -> Sequence[_T]:
        pass

    @abstractmethod
    async def update(self, entity_id: UUID, updated_entity: _T) -> Optional[_T]:
        pass

    @abstractmethod
    async def delete(self, entity_id: UUID) -> bool:
        pass

    @abstractmethod
    async def bulk_create(self, entities: Sequence[_T]) -> Sequence[_T]:
        pass

    @abstractmethod
    async def bulk_update(self, entities: Sequence[_T]) -> Sequence[_T]:
        pass

    @abstractmethod
    async def bulk_delete(self, entity_ids: Sequence[UUID]) -> int:
        pass
