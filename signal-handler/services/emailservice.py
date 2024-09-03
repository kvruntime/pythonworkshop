from .iservice import IService


class EmailService(IService):
    def notification(self, message: str):
        print(f"{self}:notifying...({message})")
        return None

    def __repr__(self) -> str:
        return f"<EmailService>"
