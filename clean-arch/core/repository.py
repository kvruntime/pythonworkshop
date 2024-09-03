# coding:utf-8
import typing

from core.entities import BaseEntity, Todo, User

T = typing.TypeVar("T", bound=BaseEntity)


class IRepositoy(typing.Generic[T], typing.Protocol):
    def get(self, id: str) -> typing.Optional[T]: ...

    def getall(self) -> typing.List[T]: ...


class IUserRepository(IRepositoy[User]): ...


class ITodoRepository(IRepositoy[Todo]): ...
