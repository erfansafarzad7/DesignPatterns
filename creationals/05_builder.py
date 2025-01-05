"""
    Builder
        - Allows constructing complex objects step by step. It lets you produce different types
        and representations of an object using the same construction code.
"""
import abc


class Car:
    def __init__(self):
        self._body = None
        self._engine = None
        self._wheel = None

    def set_body(self, body):
        self._body = body

    def set_engine(self, engine):
        self._engine = engine

    def set_wheel(self, wheel):
        self._wheel = wheel

    def detail(self):
        print(f'Body: {self._body.shape}')
        print(f'Engine: {self._engine.hp}')
        print(f'Wheel: {self._wheel.size}')

# ==============================================


class AbstractBuilder(abc.ABC):

    @abc.abstractmethod
    def get_body(self): pass

    @abc.abstractmethod
    def get_engine(self): pass

    @abc.abstractmethod
    def get_wheel(self): pass


class Benz(AbstractBuilder):
    def get_body(self):
        body = Body()
        body.shape = 'Suv'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 520
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 23
        return wheel


class Bmw(AbstractBuilder):
    def get_body(self):
        body = Body()
        body.shape = 'Sedan'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 490
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

# ==============================================


class Director:
    _builder = None

    def set_builder(self, builder):
        self._builder = builder

    def constructor(self):
        car = Car()
        car.set_body(self._builder.get_body())
        car.set_engine(self._builder.get_engine())
        car.set_wheel(self._builder.get_wheel())
        return car


class Body: shape = None
class Engine: hp = None
class Wheel: size = None

# ==============================================


def client_builder(builder):
    builders = {
        'benz': Benz,
        'bmw': Bmw,
    }

    car = builders[builder]()
    director = Director()
    director.set_builder(car)
    result = director.constructor()
    return result.detail()


if __name__ == "__main__":
    client_builder('benz')
