import sys

from PyQt6.QtWidgets import *

from di_builder import di
from form import SomeForm
from pages import HomePage, UserPage
from services import DataService
from viewmodels import FormViewModel, HomeViewModel, UserViewModel
from navigations import Shell


class Application(QApplication):
    def __init__(self) -> None:
        super().__init__([])

        self.tabPage = QTabWidget()
        self.tabPage.tabBar().hide()
        self.tabPage.setMinimumSize(400, 400)

        self.tabPage.addTab(di.resolve(HomePage), "HomePage")
        self.tabPage.addTab(di.resolve(UserPage), "UserPage")
        Shell.Current.add_outlet(self.tabPage)
        Shell.Current.register_route("home", di.resolve(HomePage))
        Shell.Current.register_route("user", di.resolve(UserPage))
        return

    def run(self) -> None:
        self.tabPage.show()
        sys.exit(self.exec())


di.add_transient(DataService)
di.add_singleton(HomePage)
di.add_singleton(UserPage)
di.add_singleton(HomeViewModel)
di.add_singleton(UserViewModel)
di.add_singleton(FormViewModel)
di.add_transient(SomeForm)


di.add_singleton(Application)
