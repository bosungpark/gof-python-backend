from abc import ABC

# 1. class로 구현
class AbstractComponent(ABC):
    def operation(self):
        raise NotImplementedError 


class AbstractDecorator(AbstractComponent):
    def __init__(self, component: AbstractComponent):
        self.component = component


class Component(AbstractComponent):
    def operation(self):
        print('Now Component working!') 


class Decorator(AbstractDecorator):
    def operation(self):
        print("wrap started")
        self.component.operation()
        print("wrap ended")


component1 = Component()
decorator1 = Decorator(component=component1)

decorator1.operation()
# wrap started
# Now Component working!
# wrap ended


# 2. wrap 활용
from functools import wraps

def decorator2(func):
    @wraps(func)
    def wrapper():
        print("wrap started, using @wraps")
        func()
        print("wrap ended, using @wraps")
    return wrapper

@decorator2
def component2():
    print('Now Component working!')

component2()
# wrap started, using @wraps
# Now Component working!
# wrap ended, using @wraps
