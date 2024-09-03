

from abc import ABC, abstractmethod


class IService(ABC):

    @abstractmethod
    def notification(self, message: str):
        return None
