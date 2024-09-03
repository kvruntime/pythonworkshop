import random


class DataService:
    def __init__(self) -> None:
        self.current_nbre = random.randint(1, 100)
        return

    def provide_data(self) -> int:
        return 2 + self.current_nbre

    def launch_operation(self) -> None:
        print(f"Operation....{self.current_nbre}")
        return None
