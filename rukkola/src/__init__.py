from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from rukkola.src.adapter.repository.sqlalchemy.tx.tx_sqlalchemy import SQLAlchemyTx
from rukkola.src.adapter.repository.sqlalchemy.user.user_sqlalchemy_repository import (
    SQLAlchemyUserRepository,
)
from rukkola.src.delivery.http.user_http import UserHandler
from rukkola.src.port.service_composer.service_composer_port import ServiceComposer
from rukkola.src.port.user.user_port import UserServiceDTO
from rukkola.src.service.user.user_service import UserService


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_async_engine("sqlite+aiosqlite:///db.sql")

    tx = SQLAlchemyTx(async_sessionmaker(engine))

    service_composer = ServiceComposer()

    user_service = UserService(
        repo=SQLAlchemyUserRepository(),
        service_composer=service_composer,
        tx=tx,
    )

    service_composer(
        user_service=user_service,
    )

    await service_composer.user_service.create(
        cmd=UserServiceDTO.Create.Command(name="ivan"),
    )

    user_router = APIRouter(prefix="/users", tags=["users"])
    UserHandler(
        service_composer=service_composer,
    )(user_router)
    app.include_router(user_router)

    yield


def main():
    return FastAPI(lifespan=lifespan)
