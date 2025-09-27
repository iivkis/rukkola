from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from rukkola.src.port.storage.tx_port import TxPort


class SQLAlchemyTx(TxPort[AsyncEngine, AsyncSession]):
    def __init__(self, conn: AsyncEngine, session: AsyncSession | None = None):
        self._conn = conn
        self._session = session

    @asynccontextmanager
    async def session(
        self,
    ) -> AsyncIterator[AsyncSession]:
        async with AsyncSession(self._conn) as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise

    @asynccontextmanager
    async def unit_of_work(
        self,
        tx: "TxPort[AsyncEngine, AsyncSession] | None" = None,
    ) -> AsyncIterator["TxPort[AsyncEngine, AsyncSession]"]:
        if self._session is None:
            async with self.session() as session:
                yield SQLAlchemyTx(
                    conn=self._conn,
                    session=session,
                )
        else:
            yield SQLAlchemyTx(
                conn=self._conn,
                session=self._session,
            )
