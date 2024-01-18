from simple_injection import ServiceCollection

from app.repository import IRepositoy, UserRepository
from app.usecase import IUserUseCase, UserUseCase


class Application:
    def __init__(self, us: IUserUseCase) -> None:
        self._us = us
        return

    def display_user_name(self, user_id: str) -> None:
        user_name = self._us.get_user_name("2")
        print(f"username->{user_name}")
        return None


di = ServiceCollection()
di.add_singleton(IRepositoy, UserRepository)
di.add_singleton(IUserUseCase, UserUseCase)
di.add_singleton(Application)

app = di.resolve(Application)
