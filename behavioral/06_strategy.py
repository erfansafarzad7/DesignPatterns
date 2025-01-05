"""
    Strategy
        - A behavioral design pattern that enables you to define a family of algorithms,
        encapsulate each one in a separate class, and make their objects interchangeable.
"""
import abc


class Read:
    def __init__(self, sentence):
        self.sentence = sentence
        self._direction = None

    def set_direction(self, direction):
        self._direction = direction

    def read(self):
        return self._direction.direct(self.sentence)

# ==============================================


class Direction(abc.ABC):

    @abc.abstractmethod
    def direct(self, data):
        pass


class Right(Direction):
    def direct(self, data):
        print(data[::-1])


class Left(Direction):
    def direct(self, data):
        print(data[::1])


if __name__ == "__main__":
    c = Read('Hello World!')
    c.set_direction(Right())
    c.read()

    c.set_direction(Left())
    c.read()
