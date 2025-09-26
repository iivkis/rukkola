from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI

from rukkola.src.delivery.http.user_http import UserHandler
from rukkola.src.port.service_composer.service_composer_port import ServiceComposer
from rukkola.src.service.user.user_service import UserService


@asynccontextmanager
async def lifespan(app: FastAPI):
    service_composer = ServiceComposer()

    user_service = UserService(
        service_composer=service_composer,
    )

    service_composer(
        user_service=user_service,
    )

    user_router = APIRouter(prefix="/users", tags=["users"])
    UserHandler(
        service_composer=service_composer,
    )(user_router)
    app.include_router(user_router)

    yield


def main():
    return FastAPI(lifespan=lifespan)
