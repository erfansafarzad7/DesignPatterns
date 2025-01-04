"""
    Factory
        - Provides an interface for creating objects in a superclass but allows subclasses
        to alter the type of objects that will be created.

"""
from abc import ABC, abstractmethod


class File(ABC):
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        product = self.make()
        return product.edit(self.file)

# ==============================================


class JsonFile(File):
    def make(self):
        return Json()


class XmlFile(File):
    def make(self):
        return Xml()

# ==============================================


class Json:
    def edit(self, file):
        return f'Working Json On {file}...'


class Xml:
    def edit(self, file):
        return f'Working Xml On {file}...'

# ==============================================


def client(file, format_):
    formats = {
        'json': JsonFile,
        'xml': XmlFile,
    }
    return formats[format_](file).call_edit()


if __name__ == "__main__":
    print(client('Example File', 'json'))
