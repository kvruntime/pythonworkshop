import typing

from core.entities import User


class IRepositoy:
    def get_user(self, user_id: str) -> typing.Optional[User]:
        raise NotImplementedError()


class UserRepository(IRepositoy):
    def __init__(self) -> None:
        super().__init__()
        self._users: typing.List[User] = [
            User(id="1", name="viktor"),
            User(id="2", name="jean"),
        ]
        return

    def get_user(self, user_id: str) -> typing.Optional[User]:
        for u in self._users:
            if u.id == user_id:
                return u
        return None
