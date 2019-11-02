from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

class SimpleCommand(Command):

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")

class ComplexCommand(Command):