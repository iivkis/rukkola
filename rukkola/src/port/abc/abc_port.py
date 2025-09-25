from abc import ABC

from dependency_injector.wiring import Provide, inject

from rukkola.src.port.di import ServiceDIPort
from rukkola.src.port.user import UserServicePort


class BaseService(ABC):
    @inject
    def __init__(
        self,
        user_service: UserServicePort = Provide[ServiceDIPort.user_service],
    ):
        self._user_service = user_service
