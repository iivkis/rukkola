from typing import Any, TypeAlias

from sqlalchemy import DateTime, String, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from rukkola.src.adapter.repository.sqlalchemy.abc import BaseModel
from rukkola.src.port.storage import TxPort
from rukkola.src.port.user.user_port import UserRepositoryDTO, UserRepositoryPort


class UserModel(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text(
            "NOW()",
        ),
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
