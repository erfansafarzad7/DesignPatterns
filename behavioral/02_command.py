"""
    Command
        - A behavioral design pattern that turns a request into a stand-alone object containing all information
        about the request. This transformation allows you to parameterize methods with requests,
        delay or queue a request's execution, and support undoable operations.
"""
import abc


class Command(abc.ABC):

    @abc.abstractmethod
    def execute(self):
        pass


class SimpleCommand(Command):
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        print(f'Simple command: i can do simple things like printing ({self._payload})')


class ComplexCommand(Command):
    def __init__(self, receiver, a, b):
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        print('Complex command: complex stuff should be done a receiver objects', end='')
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

# ==============================================


class Receiver:
    def do_something(self, a):
        print(f'\nReceiver: working on ({a})', end='')

    def do_something_else(self, b):
        print(f'\nReceiver: working on ({b})', end='')


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command):
        self._on_start = command

    def set_on_finish(self, command):
        self._on_finish = command

    def operation(self):
        self._on_start.execute()
        self._on_finish.execute()

# ==============================================


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand('Say Hi!!'))

    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, 'Sending Email..', 'Saving Data..'))

    invoker.operation()
