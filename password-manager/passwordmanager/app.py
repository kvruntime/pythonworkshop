from PyQt6.QtWidgets import QApplication
from passwordmanager.pagemain import PageMain
from passwordmanager.controller import PasswordManagerController
from passwordmanager.model import PasswordModel
import sys

from passwordmanager import STYLE_FILE


def run_app():
    application = QApplication(sys.argv)
    application.setStyle("fusion")
    # application.setStyleSheet(STYLE_FILE.read_text())
    manager = PageMain()
    passmodel = PasswordModel()
    passcontroller = PasswordManagerController(view=manager, model=passmodel)
    manager.show()
    sys.exit(application.exec())
