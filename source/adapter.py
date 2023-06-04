class AM_Redio:
    def turn_on_am_radio(self):
        print("turn on the redio AM")


class FM_Redio:
    def turn_on_fm_radio(self):
        print("turn on the redio FM")


class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    
am_radio = AM_Redio()
fm_radio = FM_Redio()

radio1 = Adapter(obj=am_radio, turn_on=am_radio.turn_on_am_radio)
radio1.turn_on()  # turn on the redio AM

radio2 = Adapter(obj=fm_radio, turn_on=fm_radio.turn_on_fm_radio)
radio2.turn_on()  # turn on the redio FM
