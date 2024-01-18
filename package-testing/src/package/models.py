import random
import typing
from dataclasses import dataclass


@dataclass
class Phone:
    name: str
    phone: str


class PhoneBook:
    def __init__(self, filename: str) -> None:
        self.phones: dict[str, Phone] = dict()
        pass

    def add(self, phone: Phone) -> None:
        self.phones.update({phone.name: Phone})
        return

    def lookup(self, name: str) -> Phone:
        return self.phones[name]

    def clear(self) -> None:
        return self.phones.clear()


class Sensor:
    def sample_value(self) -> int:
        return random.randint(0, 30)


class Alarm:
    def __init__(self, sensor: typing.Optional[Sensor] = None) -> None:
        self.high_value: int = 21
        self.low_value: int = 7
        self.sensor = sensor or Sensor()
        self.alarm_on: bool = False
        self.pressure: int = 0
        return

    def check_alarm(self) -> None:
        self.pressure = self.sensor.sample_value()
        if self.pressure >= self.high_value or self.pressure <= self.low_value:
            self.alarm_on = True
        return None
