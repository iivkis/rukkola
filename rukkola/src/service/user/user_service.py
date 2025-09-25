from datetime import datetime

from rukkola.src.domain.user.user_model import UserModel
from rukkola.src.port.abc import BaseService
from rukkola.src.port.storage import TxPort
from rukkola.src.port.user import UserServiceDTO, UserServicePort


class UserService(BaseService, UserServicePort):
    async def create(
        self, cmd: UserServiceDTO.Create.Command, tx: TxPort | None = None
    ):
        raise NotImplementedError

    async def get_user(
        self, query: UserServiceDTO.GetUser.Query, tx: TxPort | None = None
    ) -> UserModel:
        return UserModel(
            id=query.user_id,
            created_at=datetime.now(),
            name="username",
        )
