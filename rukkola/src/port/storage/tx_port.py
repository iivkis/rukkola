from abc import abstractmethod
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Generic, Protocol, TypeVar

C = TypeVar("C", covariant=False)
T = TypeVar("T", covariant=False)


class TxPort(Protocol, Generic[C, T]):
    _conn: C

    @abstractmethod
    def __init__(self, conn: C):
        raise NotImplementedError

    @abstractmethod
    @asynccontextmanager
    def session(self) -> AsyncIterator[T]:
        raise NotImplementedError

    @abstractmethod
    @asynccontextmanager
    def unit_of_work(
        self,
        tx: "TxPort[C, T] | None" = None,
    ) -> AsyncIterator["TxPort[C, T]"]:
        raise NotImplementedError
