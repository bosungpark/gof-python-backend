class Publisher:
    def __init__(self):
        self.__observers = []
    
    def register(self, observer):
        self.__observers.append(observer)
    
    def notifyAll(self, message: str):
        for observer in self.__observers:
            observer.notify(message)
            

class Observer:
    def __init__(self, name: str):
        self.name = name

    def register(self, publisher: Publisher):
        publisher.register(self)
    
    def notify(self, message: str):
        print(f"{self.name} got {message}!")
        


publisher = Publisher()

observer1 = Observer(name='observer1')
observer1.register(publisher=publisher)
observer2 = Observer(name='observer2')
observer2.register(publisher=publisher)

publisher.notifyAll('notification')


# observer1 got notification!
# observer2 got notification!