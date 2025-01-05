"""
    Visitor
        - A behavioral design pattern that allows you to add new behaviors to existing class hierarchies
        without altering their code. It separates algorithms from the objects on which they operate.
"""
import abc


class PublishVehicle(abc.ABC):
    def __init__(self, dest):
        self.dest = dest

    @abc.abstractmethod
    def order_ticket(self, ordering):
        pass


class Train(PublishVehicle):
    def order_ticket(self, ordering):
        ordering.train_ticket(self)


class Bus(PublishVehicle):
    def order_ticket(self, ordering):
        ordering.bus_ticket(self)


class Plane(PublishVehicle):
    def order_ticket(self, ordering):
        ordering.plane_ticket(self)

# ==============================================


class Ticket(abc.ABC):

    @abc.abstractmethod
    def train_ticket(self, train):
        pass

    @abc.abstractmethod
    def bus_ticket(self, bus):
        pass

    @abc.abstractmethod
    def plane_ticket(self, plane):
        pass


class Order(Ticket):
    def train_ticket(self, train):
        print(f'This is a train ticket to {train.dest}')

    def bus_ticket(self, bus):
        print(f'This is a bus ticket to {bus.dest}')

    def plane_ticket(self, plane):
        print(f'This is a plane ticket to {plane.dest}')

# ==============================================


if __name__ == "__main__":
    o = Order()
    Train('Tehran').order_ticket(o)
    Bus('Shiraz').order_ticket(o)
    Plane('Mashhad').order_ticket(o)
