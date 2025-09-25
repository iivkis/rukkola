from datetime import datetime

from rukkola.src.domain.user.user_model import User, UserModel
from rukkola.src.port.storage.tx import Tx
from rukkola.src.port.user.user_port import UserServiceDTO, UserServicePort


class UserService(UserServicePort):
    async def create(self, cmd: UserServiceDTO.Create.Command, tx: Tx | None = None):
        raise NotImplementedError

    async def get_user(
        self, query: UserServiceDTO.GetUser.Query, tx: Tx | None = None
    ) -> UserModel:
        return UserModel(
            id=query.user_id,
            created_at=datetime.now(),
            name="username",
        )
