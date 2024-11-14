import uuid

from sqlalchemy import Column, UUID, String, Integer, Boolean, ForeignKey

from app.db.session import Base


class TodosModel(Base):
    __tablename__ = 'todos'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(UUID, ForeignKey("users.id"))
