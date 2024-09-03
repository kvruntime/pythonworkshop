import random

from fastapi.datastructures import Default
from messages import HomeNotifyUserMessage
from messenger import Messenger
from services import DataService


class HomeViewModel:
    def __init__(self, data_service: DataService) -> None:
        self.data_service = data_service
        self.data: str = "data"
        self.sdata: int = self.data_service.provide_data()
        Messenger.Default.register(HomeNotifyUserMessage)
        return

    def command_operation(self) -> None:
        self.data_service.launch_operation()
        number = random.randint(0, 100)
        print(f"generate number from home: n={number}")
        Messenger.Default.send(HomeNotifyUserMessage(number))
        return None


class UserViewModel:
    def __init__(self, data_service: DataService) -> None:
        self.data_service = data_service
        self.data: str = "data"
        self.sdata: int = self.data_service.provide_data()
        Messenger.Default.use(HomeNotifyUserMessage, self.get_home_notification)
        return

    def command_operation(self) -> None:
        self.data_service.launch_operation()
        return None

    def get_home_notification(self, data: int) -> None:
        print("notification from home")
        print(f"got data={data}")
        self.sdata = data
        return None


class FormViewModel:
    def __init__(self, data_service: DataService) -> None:
        self.data_service = data_service
        self.data: str = "data"
        self.sdata: int = self.data_service.provide_data()

        return

    def command_operation(self) -> None:
        self.data_service.launch_operation()
        return None
