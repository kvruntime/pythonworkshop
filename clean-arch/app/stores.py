# coding:utf-8
import typing
from typing import List

from core.entities import User
from core.repository import IUserRepository


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
