from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List
from uuid import UUID

from sqlalchemy.orm import Session

T = TypeVar('T')


class BaseRepository(ABC, Generic[T]):
    def __init__(self, db: Session):
        self.db = db

    @abstractmethod
    async def create(self, entity: T):
        pass

    @abstractmethod
    async def get(self, entity_id: UUID) -> Optional[T]:
        pass

    @abstractmethod
    async def get_all(self, limit: int = 100, offset: int = 0) -> List[T]:
        pass

    @abstractmethod
    async def update(self, entity: T) -> Optional[T]:
        pass

    @abstractmethod
    async def delete(self, entity_id: UUID) -> None:
        pass

    @abstractmethod
    async def bulk_create(self, entities: List[T]) -> List[T]:
        pass

    @abstractmethod
    async def bulk_update(self, entities: List[T]) -> List[T]:
        pass

    @abstractmethod
    async def bulk_delete(self, entity_ids: List[UUID]) -> None:
        pass

    async def begin_transaction(self):
        self.db.begin()

    async def rollback_transaction(self):
        self.db.rollback()

    async def commit(self) -> None:
        self.db.commit()

    async def refresh(self, entity: T) -> None:
        self.db.refresh(entity)

    async def refresh_bulk(self, entities: List[T]) -> None:
        for entity in entities:
            self.db.refresh(entity)
