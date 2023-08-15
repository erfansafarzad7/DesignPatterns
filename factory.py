"""
    Factory is a creational design pattern that provides an interface for creating objects
    in a superclass, but allows subclasses to alter the type of objects that will be created.
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
        result = product.edit(self.file)
        return result


class JsonFile(File):
    def make(self):
        return Json()


class XmlFile(File):
    def make(self):
        return Xml()


class Json:
    def edit(self, file):
        return f'Working Json On {file}...'


class Xml:
    def edit(self, file):
        return f'Working Xml On {file}...'


def client(file, format_):
    formats = {
        'json': JsonFile,
        'xml': XmlFile,
    }
    result = formats[format_](file)
    return result.call_edit()


print(client('Example File', 'json'))
