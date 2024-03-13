# coding:utf-8
import typing
from core.irepository import IUserRepository
from core.entities import User


class UserUseCase:
    def __init__(self, repo: IUserRepository) -> None:
        super().__init__()
        self._repo = repo
        return

    def get_user_name(self, user_id: str) -> str:
        _user = self._repo.get(user_id)
        if _user:
            return _user.name
        raise Exception()

    def get_users(self) -> typing.List[User]:
        return self._repo.getall()


class TodoUseCases:
    pass
