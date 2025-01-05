"""
    Bridge
        -The Bridge pattern is a structural design pattern that separates an abstraction from its implementation,
        allowing them to vary independently. It helps you split a large class into two separate hierarchies
        that can be developed and modified independently.
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


if __name__ == "__main__":
    blue = Blue()
    circle = Circle(blue)
    circle.show()
