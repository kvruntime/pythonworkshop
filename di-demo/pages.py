from form import SomeForm
from PyQt6.QtGui import QShowEvent
from PyQt6.QtWidgets import *
from viewmodels import FormViewModel, HomeViewModel, UserViewModel


class HomePage(QWidget):
    def __init__(self, vm: HomeViewModel, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.resize(400, 400)

        self.vm = vm

        layout = QVBoxLayout(self)

        self.label = QLabel("Service")
        self.buttonCaller = QPushButton("Caller")

        layout.addWidget(QLabel("HomePage"))
        layout.addWidget(self.label)
        layout.addWidget(self.buttonCaller)

        self.initializeBinding()
        return

    def initializeBinding(self) -> None:
        self.buttonCaller.clicked.connect(self.vm.command_operation)
        self.label.setText(f"Data: {self.vm.sdata}")
        return None


class UserPage(QWidget):
    def __init__(self, vm: UserViewModel, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.resize(400, 400)

        self.vm = vm

        layout = QVBoxLayout(self)

        self.label = QLabel("Service")
        self.buttonCaller = QPushButton("Caller")
        self.buttonOpenDialog = QPushButton("Open Dialog")

        layout.addStrut(10)
        layout.addWidget(QLabel("UserPage"))
        layout.addWidget(self.label)
        layout.addWidget(self.buttonCaller)
        layout.addWidget(self.buttonOpenDialog)
        layout.addStrut(50)

        self.initializeBinding()
        return

    def initializeBinding(self) -> None:
        # self.buttonCaller.clicked.connect(self.vm.command_operation)
        self.buttonCaller.clicked.connect(self.vm.command_operation)
        self.buttonOpenDialog.clicked.connect(self.command_open)
        self.label.setText(f"Data: {self.vm.sdata}")
        return None

    def command_open(self) -> None:
        from di_builder import di

        dlg = SomeForm(di.resolve(FormViewModel), self)
        dlg.exec()
        return None

    def showEvent(self, a0: QShowEvent | None) -> None:
        self.label.setText(f"Data: {self.vm.sdata}")
        return super().showEvent(a0)
