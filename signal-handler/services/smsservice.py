from .iservice import IService


class SmsService(IService):
    def notification(self, message: str):
        print(f"{self}:sending...({message})")
        return None

    def __repr__(self) -> str:
        return f"<SmsService>"
