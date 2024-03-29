from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

class SimpleCommand(Command):

    def __init__(self, payload: str):
        self._payload = payload

    def execute(self):
        print(f"test"
              f"({self._payload})")

class ComplexCommand(Command):

    def __init__(self, receiver: Receiver, a: str, b: str):
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        print("test")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

class Receiver:
    def do_something(self, a: str):
        print("do sth")

    def do_something_else(self, b: str):
        print("do sth else")

class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        print("invoke")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("test")

        print("Invoker: finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()

if __name__ == "__main__":

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("testtest"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
    receiver, "Send email", "Save report"))

    invoker.do_something_important()
