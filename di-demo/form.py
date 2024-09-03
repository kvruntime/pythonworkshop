from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget

from viewmodels import FormViewModel


class SomeForm(QDialog):
    def __init__(self, vm: FormViewModel, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.vm = vm
        self.button = QPushButton("Caller")

        layout = QVBoxLayout(self)
        layout.addWidget(QDial(self))
        layout.addWidget(self.button)

        self.button.clicked.connect(self.vm.command_operation)
        return
