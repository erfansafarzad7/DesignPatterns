"""
    Adapter Design Pattern
        - A structural design pattern that allows objects with incompatible interfaces to collaborate.
        This example demonstrates converting XML data to JSON format for compatibility.
"""
import xmltodict


class Application:
    def send_request(self):
        return 'adapter.xml'


class Analytic:
    def receive_request(self, json):
        return json


class Adapter:
    def convert_xml_json(self, file):
        with open(file, 'r') as f:
            obj = xmltodict.parse(f.read())
            return obj

# ==============================================


def client_adapter():
    sender = Application().send_request()
    converted_data = Adapter().convert_xml_json(sender)
    receiver = Analytic().receive_request(converted_data)
    print(receiver)


if __name__ == "__main__":
    client_adapter()
