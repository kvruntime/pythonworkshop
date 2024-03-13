# coding:utf-8
from app.stores import UserInMemoryRepository
from app.usecases import UserUseCase
from core.repository import IUserRepository
from simple_injection import ServiceCollection


class Application:
    def __init__(self, us: UserUseCase) -> None:
        self._us = us
        return

    def launch(self) -> None:
        user_name = self._us.get_user_name("2")
        print(f"username->{user_name}")
        print(f"All Users: {self._us.get_users()}")
        return None


di = ServiceCollection()
di.add_singleton(IUserRepository, UserInMemoryRepository)
di.add_singleton(UserUseCase)
di.add_singleton(Application)
app = di.resolve(Application)
