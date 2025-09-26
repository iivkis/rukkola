from rukkola.src.port.user.user_port import UserServicePort


class ServiceComposer:
    def __call__(self, user_service: UserServicePort):
        self.user_service = user_service
