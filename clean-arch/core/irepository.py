# coding:utf-8
import typing

from core.entities import BaseEntity, Todo, User

T = typing.TypeVar("T", bound=BaseEntity)


class IRepositoy(typing.Generic[T], typing.Protocol):
    def get(self, id: str) -> typing.Optional[T]:
        raise NotImplementedError()

    def getall(self) -> typing.List[T]:
        raise NotImplementedError()


class IUserRepository(IRepositoy[User]):
    def get(self, id: str) -> User | None:
        raise NotImplementedError()


class ITodoRepository(IRepositoy[Todo]):
    def get(self, id: str) -> Todo | None:
        raise NotImplementedError()
