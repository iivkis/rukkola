from fastapi import APIRouter, FastAPI

from rukkola.src.delivery.http.user_http import UserHandler
from rukkola.src.service.user.user_service import UserService


def main():
    app = FastAPI()

    user_router = APIRouter(
        prefix="/users",
        tags=["users"],
    )

    user_service = UserService()

    UserHandler()(user_router)

    app.include_router(user_router)

    return app
