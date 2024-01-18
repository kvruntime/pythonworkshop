from app.repository import IRepositoy


class IUserUseCase:
    def __init__(self, repo: IRepositoy) -> None:
        self._repo = repo
        return

    def get_user_name(self, user_id: str) -> str:
        raise NotImplementedError()


class UserUseCase(IUserUseCase):
    def __init__(self, repo: IRepositoy) -> None:
        super().__init__(repo)
        return

    def get_user_name(self, user_id: str) -> str:
        _user = self._repo.get_user(user_id)
        if _user:
            return _user.name
        raise Exception()
