from typing import Optional, Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status

from app.core.database import get_db
from app.dependency_injection.service_registry import get_user_service
from app.models.books_db_context.user_model import UserModel
from app.services.user_service import UserService


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "codingwithroby",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2029,
            }
        }
    }


router = APIRouter(prefix="/user", tags=["user"])

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(db: db_dependency):
    result = db.query(UserModel).filter(UserModel.id == "1").first()
    return result


@router.get("/users/{user_id}")
async def get_user(user_id: int,
                   user_service: UserService = Depends(get_user_service),
                   user_service2: UserService = Depends(get_user_service)):
    user = await user_service.get_user(user_id)
    user2 = await user_service2.get_user(user_id)
    return user


@router.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    result = 1
    return result
