from ..repositories.user_repository import UserRepository


class UserService:

    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository


    def register_user(self, user_data) -> None:
        pass
