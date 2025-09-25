from datetime import datetime
from typing import Any

from fastapi import APIRouter, FastAPI

from rukkola.src.domain.user.user_model import UserModel


class UserHandler:
    def __init__(self): ...

    def __call__(self, user_router: APIRouter):
        @user_router.get("/{id}")
        async def get_user(id: int) -> UserModel:
            return UserModel(
                id=id,
                created_at=datetime.now(),
                name="username",
            )
