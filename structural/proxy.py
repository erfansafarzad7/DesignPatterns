"""
    Proxy
    - a structural design pattern that lets provide a substitute or placeholder
    for another object. A proxy controls access to the original object, allowing you
    to perform something either before or after the request gets through to the original object.
"""
import abc
import time
import datetime


class AbstractServer(abc.ABC):

    @abc.abstractmethod
    def receive(self):
        pass


class Server(AbstractServer):
    def receive(self):
        print('Processing your request...')
        time.sleep(2)
        print('Done!..')


class LogProxy(AbstractServer):
    def __init__(self, server):
        self._server = server

    def receive(self):
        self.logging()
        # code..
        self._server.receive()

    def logging(self):
        with open('log.log', 'a') as log:
            log.write(f'Request {datetime.datetime.now()}')


def client_server(server, proxy):
    s = server()
    p = proxy(s)
    p.receive()


client_server(Server, LogProxy)
