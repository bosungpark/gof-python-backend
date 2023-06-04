# 1. __new__
class Singleton1(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            print('create')
            cls.instance = super(Singleton1, cls).__new__(cls)
        else:
            print('recycle')
        return cls.instance
    
singleton1_1 = Singleton1()  # create
singleton1_2 = Singleton1()  # recycle
assert singleton1_1 == singleton1_2


# 2. lazy instantiation 
class Singleton2:
    _instance = None
    def __init__(self):
        if not Singleton2._instance:
            print('__init__')
        else:
            print('instance already created:', self.getInstance())
 
    @classmethod
    def create_instance(cls):
        if not cls._instance:
            cls._instance = Singleton2()
        return cls._instance
    
singleton2_1 = Singleton2() #  __init__, not singleton

singleton2_2 = Singleton2.create_instance()  # __init__, singleton
singleton2_3 = Singleton2.create_instance()
assert singleton2_1 != singleton2_2 and singleton2_1 != singleton2_3
assert singleton2_2 == singleton2_3
singleton2_4 = Singleton2.create_instance()
assert singleton2_2 == singleton2_4


# 3. monostate singleton, 객체의 유무보다는 상태를 균일하게 만드는 것에 집중하는 패턴
class Singleton3:
    __shared_state = dict()
    def __init__(self):
        self.__dict__ = self.__shared_state

singleton3_1 = Singleton3()
singleton3_2 = Singleton3()
assert singleton3_1 != singleton3_2  # it is not same object!

singleton3_1.a = 1
assert singleton3_1.a == 1 and singleton3_2.a == 1  # shares state

singleton3_2.b = 2
assert singleton3_1.b == 2 and singleton3_2.b == 2  # shares state
