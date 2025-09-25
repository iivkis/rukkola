from fastapi import APIRouter, FastAPI

from rukkola.src.delivery.http.user_http import UserHandler
from rukkola.src.service.di.di_service import ServiceDI


def main():
    service_di = ServiceDI()
    service_di.wire(modules=[__name__])

    app = FastAPI()

    user_router = APIRouter(
        prefix="/users",
        tags=["users"],
    )

    UserHandler()(user_router)

    app.include_router(user_router)

    return app
