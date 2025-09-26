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
        self, cmd: UserServiceDTO.Create.Command, tx: TxPort | None = None
    ):
        await self._repo.create(
            cmd=UserRepositoryDTO.Create.Command(name=""),
            tx=self.tx,
        )

        raise NotImplementedError

    async def get_user(
        self, query: UserServiceDTO.GetUser.Query, tx: TxPort | None = None
    ) -> UserEntity:
        return UserEntity(
            id=query.user_id,
            created_at=datetime.now(),
            name="username",
        )
