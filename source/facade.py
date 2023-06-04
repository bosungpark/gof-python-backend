class Redio:
    def turn_on(self):
        print("turn on the redio")

class TV:
    def turn_on(self):
        print("turn on the TV")

class Facade:
    def __init__(self):
        self.redio = Redio()
        self.tv = TV()

    def turn_on_every_electronics(self):
        self.redio.turn_on()
        self.tv.turn_on()

facade = Facade()
facade.turn_on_every_electronics()

# turn on the redio
# turn on the TV   
   