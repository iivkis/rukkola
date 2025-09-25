from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol

from rukkola.src.domain.user.user_model import User, UserModel
from rukkola.src.port.storage.tx import Tx


class UserServiceDTO:
    class Create:
        @dataclass
        class Command: ...

    class GetUser:
        @dataclass
        class Query:
            user_id: User.ID


class UserServicePort(Protocol):
    @abstractmethod
    async def create(self, cmd: UserServiceDTO.Create.Command, tx: Tx | None = None):
        raise NotImplementedError

    @abstractmethod
    async def get_user(
        self, query: UserServiceDTO.GetUser.Query, tx: Tx | None = None
    ) -> UserModel:
        raise NotImplementedError


class UserRepositoryDTO:
    class Create:
        @dataclass
        class Command: ...


class UserRepositoryPort(Protocol):
    @abstractmethod
    async def create(self, cmd: UserRepositoryDTO.Create.Command, tx: Tx | None = None):
        raise NotImplementedError
