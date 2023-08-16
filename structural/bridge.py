"""
    Bridge
    - a structural design pattern that lets you split a large class into two separate
    hierarchies - abstraction and implementation - which can be developed independently at each other.
"""
import abc


class Shape(abc.ABC):
    def __init__(self, color):
        self.color = color

    def show(self):
        pass


class Circle(Shape):
    def show(self):
        self.color.paint(self.__class__.__name__)


class Square(Shape):
    def show(self):
        self.color.paint(self.__class__.__name__)


class Color(abc.ABC):
    def paint(self, name):
        pass


class Blue(Color):
    def paint(self, name):
        print(f'this is a blue {name}')


class Red(Color):
    def paint(self, name):
        print(f'this is a red {name}')


blue = Blue()
circle = Circle(blue)
circle.show()
