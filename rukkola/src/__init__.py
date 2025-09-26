from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, FastAPI

from rukkola.src.port.composer.composer_port import ServiceComposer
from rukkola.src.port.user.user_port import UserServicePort
from rukkola.src.service.user.user_service import UserService


class DIContainer(containers.DeclarativeContainer):
    service_composer = ServiceComposer()

    user_service = providers.Factory(
        UserService,
        service_composer,
    )


@inject
def main(
    service_composer: ServiceComposer = Provide[DIContainer.service_composer],
    user_service: UserServicePort = Provide[DIContainer.user_service],
):
    service_composer(
        user_service=user_service,
    )

    app = FastAPI()

    user_router = APIRouter(
        prefix="/users",
        tags=["users"],
    )

    app.include_router(user_router)

    return app


if __name__ == "__main__":
    di = DIContainer()
    di.wire(modules=[__name__])
