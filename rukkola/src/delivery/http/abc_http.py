from abc import ABC

from dependency_injector.wiring import Provide, inject

from rukkola.src.port.di.di_port import ServiceDIPort
from rukkola.src.port.user.user_port import UserServicePort


class BaseHandler(ABC):
    @inject
    def __init__(
        self,
        user_service: UserServicePort = Provide[ServiceDIPort.user_service],
    ):
        self._user_service = user_service
