# -*- coding:utf-8 -*-
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import *

from viewmodels.home_vm import HomeViewModel


class MainPage(QWidget):
    message = pyqtSignal(str)

    def __init__(self, vm: HomeViewModel):
        super().__init__()
        self.vm = vm
        self.initialize_component()
        self.initialize_binding()
        pass

    def initialize_component(self):
        self.resize(400, 400)

        self.btn = QPushButton(self.tr("Send"))
        self.msg_tbox = QLineEdit()
        self.msg_tbox.setPlaceholderText("edit message here")

        self.sms = QCheckBox("sms: subscribe")
        self.email = QCheckBox("email:subscribe")

        layout = QVBoxLayout(self)
        layout.addWidget(self.msg_tbox)
        layout.addWidget(self.btn)
        layout.addStretch()
        layout.addWidget(self.sms)
        layout.addWidget(self.email)
        return None

    def initialize_binding(self):
        self.btn.clicked.connect(
            lambda: self.vm.notification(self.msg_tbox.text().strip())
        )
        self.sms.clicked.connect(self.vm.subscribe_sms)
        self.email.clicked.connect(self.vm.subscribe_email)
        return None
