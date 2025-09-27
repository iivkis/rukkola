from datetime import datetime

from rukkola.src.domain.user.user_domain import UserEntity
from rukkola.src.port.abc import BaseService
from rukkola.src.port.storage import TxPort
from rukkola.src.port.user import UserServiceDTO, UserServicePort
from rukkola.src.port.user.user_port import UserRepositoryDTO, UserRepositoryPort


class UserService(BaseService, UserServicePort):
    def __init__(
        self,
        repo: UserRepositoryPort,
        **kwargs,
    ):
        self._repo = repo
        super().__init__(**kwargs)

    async def create(
        self,
        cmd: UserServiceDTO.Create.Command,
        uof: TxPort | None = None,
    ):
        await self._repo.create(
            cmd=UserRepositoryDTO.Create.Command(
                name=cmd.name,
            ),
            tx=self.tx,
        )

    async def get_user(
        self,
        query: UserServiceDTO.GetUser.Query,
        uof: TxPort | None = None,
    ) -> UserEntity:
        return UserEntity(
            id=query.user_id,
            created_at=datetime.now(),
            name="username",
        )

    async def get_users(self, uof: TxPort | None = None) -> list[UserEntity]:
        return await self._repo.get_users(tx=self.tx)
