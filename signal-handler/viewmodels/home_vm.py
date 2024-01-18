# -*- coding:utf-8 -*-
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import QObject

from services.iservice import IService
from services import EmailService, SmsService


class HomeViewModel(QObject):
    message = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.es = EmailService()
        self.ss = SmsService()
        pass

    def subscribe_to_message(self, service: IService):
        self.message.connect(service.notification)
        return None

    def unsubscribe_to_message(self, service: IService):
        self.message.disconnect(service.notification)
        return None

    def notification(self, msg: str):
        if msg:
            self.message.emit(msg)
        return None

    def subscribe_sms(self, state: bool):
        if state:
            self.subscribe_to_message(self.ss)
            return
        self.unsubscribe_to_message(self.ss)
        return None

    def subscribe_email(self, state: bool):
        if state:
            self.subscribe_to_message(self.es)
            return
        self.unsubscribe_to_message(self.es)
        return None
