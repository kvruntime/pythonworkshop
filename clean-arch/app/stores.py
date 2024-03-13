# coding:utf-8
from typing import List
from core.irepository import IUserRepository
from core.entities import User
import typing


class UserInMemoryRepository(IUserRepository):
    def __init__(self) -> None:
        super().__init__()
        self._users: typing.List[User] = [
            User(id="1", name="viktor"),
            User(id="2", name="jean"),
        ]
        return

    def get(self, id: str) -> typing.Optional[User]:
        for u in self._users:
            if getattr(u, "id"):
                if getattr(u, "id") == id:
                    return u
        return None

    def getall(self) -> List[User]:
        return self._users
