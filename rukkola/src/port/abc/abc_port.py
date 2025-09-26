from abc import ABC

from rukkola.src.port.composer import ServiceComposer


class BaseService(ABC):
    def __init__(
        self,
        service_composer: ServiceComposer,
    ):
        self.sc = service_composer
