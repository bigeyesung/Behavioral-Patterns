from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

class SimpleCommand(Command):

    def __init__(self, payload: str) -> None:
        self._payload = payload