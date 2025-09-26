from abc import abstractmethod
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Generic, Protocol, TypeVar

C = TypeVar("C", covariant=True)
T = TypeVar("T", covariant=False)


class TxPort(Protocol, Generic[C, T]):
    _conn: C

    def __init__(self, conn: C):
        raise NotImplementedError

    @abstractmethod
    @asynccontextmanager
    def __call__(self, tx: "T | None" = None) -> AsyncIterator[T]:
        raise NotImplementedError
