from abc import ABC

from rukkola.src.port.service_composer import ServiceComposer


class BaseHandler(ABC):
    def __init__(
        self,
        service_composer: ServiceComposer,
    ):
        self.sc = service_composer
