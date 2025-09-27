from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol

from rukkola.src.domain.user.user_domain import User, UserEntity
from rukkola.src.port.storage import TxPort


class UserServiceDTO:
    class Create:
        @dataclass
        class Command:
            name: str

    class GetUser:
        @dataclass
        class Query:
            user_id: User.ID


class UserServicePort(Protocol):
    @abstractmethod
    async def create(
        self, cmd: UserServiceDTO.Create.Command, uof: TxPort | None = None
    ):
        raise NotImplementedError

    @abstractmethod
    async def get_user(
        self, query: UserServiceDTO.GetUser.Query, uof: TxPort | None = None
    ) -> UserEntity:
        raise NotImplementedError


class UserRepositoryDTO:
    class Create:
        @dataclass
        class Command:
            name: str


class UserRepositoryPort(Protocol):
    @abstractmethod
    async def create(
        self,
        cmd: UserRepositoryDTO.Create.Command,
        tx: TxPort,
    ):
        raise NotImplementedError
