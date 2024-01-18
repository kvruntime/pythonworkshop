from services import DataService


class HomeViewModel:
    def __init__(self, data_service: DataService) -> None:
        self.data_service = data_service
        self.data: str = "data"
        self.sdata: int = self.data_service.provide_data()

        return

    def command_operation(self) -> None:
        self.data_service.launch_operation()
        return None


class UserViewModel:
    def __init__(self, data_service: DataService) -> None:
        self.data_service = data_service
        self.data: str = "data"
        self.sdata: int = self.data_service.provide_data()

        return

    def command_operation(self) -> None:
        self.data_service.launch_operation()
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
