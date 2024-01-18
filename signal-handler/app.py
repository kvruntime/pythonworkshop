# coding:utf-8
import sys
from PyQt6.QtWidgets import QApplication
from pages.mainpage import MainPage
from viewmodels.home_vm import HomeViewModel
from utils import (
    get_resource,
)


class SingalApp(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.setApplicationName("signal handler")
        self.setStyleSheet(
            get_resource("css/style.css").read_text(encoding="utf-8"),
        )
        self.win = MainPage(HomeViewModel())
        return

    def run(self):
        self.win.show()
        sys.exit(self.exec())
