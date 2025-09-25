from dependency_injector import containers, providers

from rukkola.src.port.user import UserServicePort


class ServiceDIPort(containers.DeclarativeContainer):
    user_service: providers.Factory[UserServicePort]
