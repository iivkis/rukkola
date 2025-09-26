from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from rukkola.src.port.storage.tx_port import TxPort


class SQLAlchemyTx(TxPort[AsyncEngine, AsyncSession]):
    def __init__(self, conn: AsyncEngine):
        self._conn = conn

    @asynccontextmanager
    async def __call__(
        self, session: AsyncSession | None = None
    ) -> AsyncIterator[AsyncSession]:
        if session is None:
            async with AsyncSession(self._conn) as new_session:
                try:
                    yield new_session
                    await new_session.commit()
                except Exception:
                    await new_session.rollback()
                    raise
        else:
            yield session
