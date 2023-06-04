import time
from abc import ABC, abstractmethod


class Data(ABC):
    def __init__(self):
        self.filename = None

    @abstractmethod
    def open(self):
        pass


class BigData(Data):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f'loading {self.filename}')
        time.sleep(10)

    def open(self):
        print(f'opening {self.filename}')


class ProxyData(Data):
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def open(self):
        if self.data is None:
            self.data = BigData(self.filename)
        self.data.open()


proxy_data = ProxyData('whatever.py')
# do something whatever takes time, some complex codes...
proxy_data.open()
