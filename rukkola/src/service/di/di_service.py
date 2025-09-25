from dependency_injector import providers

from rukkola.src.port.di import ServiceDIPort
from rukkola.src.service.user.user_service import UserService


class ServiceDI(ServiceDIPort):
    user_service = providers.Factory(
        UserService,
    )
