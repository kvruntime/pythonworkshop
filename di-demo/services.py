class DataService:
    nbre: int = 0

    def __init__(self) -> None:
        self.__class__.nbre += 1
        self.current_nbre = self.__class__.nbre
        return

    def provide_data(self) -> int:
        return 2 + self.__class__.nbre

    def launch_operation(self) -> None:
        print(f"Operation....{self.current_nbre}")
        return None
