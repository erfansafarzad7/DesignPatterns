"""
    Composite
    - a structural design pattern that lets you compose objects into tree structures
    and then work with these structures as if they were individual objects.
"""
import abc


class Being(abc.ABC):
    def add(self, child):
        pass

    def remove(self, child):
        pass

    def is_composite(self):
        return False

    @abc.abstractmethod
    def execute(self):
        pass


class Animal(Being):
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f'\tAnimal {self.name}')


class Human(Being):
    def __init__(self):
        self._children = []

    def add(self, child):
        self._children.append(child)

    def remove(self, child):
        self._children.remove(child)

    def is_composite(self):
        return True

    def execute(self):
        print('Human Composite.')

        for child in self._children:
            child.execute()


class Male(Human):
    def __init__(self, name):
        self.name = name

    def is_composite(self):
        return False

    def execute(self):
        print(f'\tMale {self.name}')


class Female(Human):
    def __init__(self, name):
        self.name = name

    def is_composite(self):
        return False

    def execute(self):
        print(f'\tFemale {self.name}')


def client_composite():
    f1 = Female('jane')
    f2 = Male('kevin')

    h = Human()
    h.add(f1)
    h.add(f2)
    h.execute()

    a = Animal('jimi')
    a.execute()


client_composite()
