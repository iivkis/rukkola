from fastapi import APIRouter

from rukkola.src.delivery.http.abc_http import BaseHandler
from rukkola.src.domain.user.user_domain import UserEntity
from rukkola.src.port.user.user_port import UserServiceDTO


class UserHandler(BaseHandler):
    def __call__(self, user_router: APIRouter):
        @user_router.get("/{id}")
        async def get_user(id: int) -> UserEntity:
            return await self.sc.user_service.get_user(
                query=UserServiceDTO.GetUser.Query(
                    user_id=1,
                ),
            )

        @user_router.get("/")
        async def get_users() -> list[UserEntity]:
            return await self.sc.user_service.get_users()
