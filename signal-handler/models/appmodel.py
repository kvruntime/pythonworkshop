
from services.emailservice import EmailService
from services.smsservice import SmsService


class AppModel:

    def __init__(self) -> None:

        self.es = EmailService()

        self.ss = SmsService()
        pass
