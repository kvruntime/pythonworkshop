# coding:utf-8
import sys
import typing

from app.stores import UserInMemoryRepository
from app.usecases import UserUseCase
from core.entities import User
from core.repository import IUserRepository
from PyQt6.QtWidgets import *
from simple_injection import ServiceCollection


class UserViewModel:
    def __init__(self, repo: IUserRepository) -> None:
        self._repo = repo
        self.users: typing.List[User] = []
        return

    def command_get_user(self) -> None:
        try:
            self.users = self._repo.getall()
        except:
            self.users = []
        return None


class UserForm(QWidget):
    def __init__(self, vm: UserViewModel):
        super().__init__()
        self.vm = vm

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("<h1>Simple Application</h1>"))
        self.button = QPushButton("Fetch User")
        self.layoutUser = QVBoxLayout()

        layout.addWidget(self.button)
        layout.addLayout(self.layoutUser)

        self.button.clicked.connect(self.vm.command_get_user)
        self.button.clicked.connect(self._update_ui)
        pass

    def _update_ui(self) -> None:
        for index in range(self.layoutUser.count()):
            self.layoutUser.removeItem(self.layoutUser.itemAt(index))
            self.layoutUser.itemAt(index)
        for child in self.layoutUser.children():
            child.deleteLater()

        for user in self.vm.users:
            self.layoutUser.addWidget(QLabel(user.name))
        return


di = ServiceCollection()
di.add_singleton(IUserRepository, UserInMemoryRepository)
di.add_singleton(UserViewModel)
di.add_singleton(UserUseCase)
di.add_singleton(UserForm)


def start_app() -> None:
    app = QApplication(sys.argv)
    w = di.resolve(UserForm)
    w.show()
    app.exec()
    return
