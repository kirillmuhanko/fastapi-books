from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, status
from jose import jwt, JWTError

from app.core.config import settings

ALGORITHM = "HS256"


class TokenGenerator:
    @staticmethod
    def create_access_token(
            username: str, user_id: str, role: str, expires_delta: timedelta
    ) -> str:
        encode = {"sub": username, "id": user_id, "role": role}
        expires = datetime.now(timezone.utc) + expires_delta
        encode.update({"exp": expires})
        return jwt.encode(encode, settings.secret_key, algorithm=ALGORITHM)

    @staticmethod
    def decode_access_token(token: str):
        try:
            payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            user_id: int = payload.get("id")
            user_role: str = payload.get("role")
            if username is None or user_id is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate user.",
                )
            return {"username": username, "id": user_id, "user_role": user_role}
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate user.",
            )
