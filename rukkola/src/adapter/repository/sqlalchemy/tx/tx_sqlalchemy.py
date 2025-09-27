from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import TypeAlias

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from rukkola.src.port.storage.tx_port import TxPort

C: TypeAlias = async_sessionmaker[AsyncSession]
T: TypeAlias = AsyncSession


class SQLAlchemyTx(TxPort[C, T]):
    def __init__(
        self,
        session_maker: async_sessionmaker[AsyncSession],
        session: AsyncSession | None = None,
    ):
        self._session_maker = session_maker
        self._session = session

    @asynccontextmanager
    async def session(
        self,
    ) -> AsyncIterator[AsyncSession]:
        @asynccontextmanager
        async def exec(session: AsyncSession):
            try:
                yield
                await session.commit()
            except Exception:
                await session.rollback()
                raise

        if self._session is None:
            async with self._session_maker() as session:
                async with exec(session):
                    yield session
        else:
            async with exec(self._session):
                yield self._session

    @asynccontextmanager
    async def unit_of_work(
        self,
        tx: "TxPort[C, T] | None" = None,
    ) -> AsyncIterator["TxPort[C, T]"]:
        if self._session is None:
            async with self.session() as session:
                yield SQLAlchemyTx(
                    session_maker=self._session_maker,
                    session=session,
                )
        else:
            yield SQLAlchemyTx(
                session_maker=self._session_maker,
                session=self._session,
            )
