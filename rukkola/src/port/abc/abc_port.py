from abc import ABC

from rukkola.src.port.service_composer import ServiceComposer
from rukkola.src.port.storage.tx_port import TxPort


class BaseService(ABC):
    def __init__(
        self,
        service_composer: ServiceComposer,
        tx: TxPort,
    ):
        self.sc = service_composer
        self.tx = tx
