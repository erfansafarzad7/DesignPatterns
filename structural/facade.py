"""
    Facade
    - a structural design pattern that provides a simplified interface to a library,
    a framework, or any other complex set of classes.
"""


class CPU:
    def execute(self):
        print('Execute...')


class Memory:
    def load(self):
        print('Loading data...')


class SSD:
    def read(self):
        print('Reading data...')


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SSD()

    def start(self):
        self.cpu.execute()
        self.memory.load()
        self.ssd.read()


def client_facade():
    computer_facade = Computer()
    computer_facade.start()


client_facade()
