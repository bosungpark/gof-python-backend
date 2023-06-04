from abc import ABCMeta, abstractmethod
from enum import Enum


class RedioType(Enum):
    FM = 'fm'
    AM = 'am'

class Redio(metaclass=ABCMeta):
    @abstractmethod
    def turn_on(self):
        ...

class RedioFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        ...


class AM_Redio(Redio):
    def turn_on(self):
        print("turn on the redio AM")


class FM_Redio(Redio):
    def turn_on(self):
        print("turn on the redio FM")


class AM_RedioFactory(RedioFactory):
    def create(self):
        return AM_Redio()


class FM_RedioFactory(RedioFactory):
    def create(self):
        return FM_Redio()


class Client():
    def turn_on(self, type):
        if type == RedioType.AM:
            factory = AM_RedioFactory()
        elif type == RedioType.FM:
            factory = FM_RedioFactory()
        else:
            return

        redio = factory.create()
        redio.turn_on()


client = Client()
client.turn_on(type=RedioType.AM)
client.turn_on(type=RedioType.FM)
