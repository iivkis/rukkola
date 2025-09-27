from datetime import datetime
from typing import Any, TypeAlias

from sqlalchemy import DateTime, String, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from rukkola.src.adapter.repository.sqlalchemy.abc.abc_sqlalchemy_repository import (
    BaseModel,
)
from rukkola.src.domain.user.user_domain import UserEntity
from rukkola.src.port.storage import TxPort
from rukkola.src.port.user.user_port import UserRepositoryDTO, UserRepositoryPort


class UserModel(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    name: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )


class SQLAlchemyUserRepository(UserRepositoryPort):
    Tx: TypeAlias = TxPort[Any, AsyncSession]

    async def create(
        self,
        cmd: UserRepositoryDTO.Create.Command,
        tx: Tx,
    ):
        async with tx.session() as session:
            session.add(
                UserModel(
                    name=cmd.name,
                )
            )

    async def get_users(self, tx: Tx) -> list[UserEntity]:
        async with tx.session() as session:
            result = await session.execute(select(UserModel))
            users = result.scalars().all()

            return [
                UserEntity(
                    id=user.id,
                    created_at=user.created_at,
                    name=user.name,
                )
                for user in users
            ]
