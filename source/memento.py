class Memento():
    def __init__(self, state):
        self.state = state
        print(f"I am a Memento and my state is {self.state}")

class Originator():   
    def __init__(self):
        self.state = ""

    def create_memento(self):
        return Memento(self.state)

    def memento(self, memento):
        self.state = memento.state        
        
        
class CareTaker():
    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def create(self):
        memento = self._originator.create_memento()
        self._mementos.append(memento)

    def restore(self, index):
        memento = self._mementos[index]
        self._originator.memento(memento)


originator = Originator()
care_taker = CareTaker(originator=originator)

originator.state = "state1"

care_taker.create()
assert originator.state == 'state1'  
originator.state = "state2"

care_taker.restore(0)
assert originator.state == 'state1'