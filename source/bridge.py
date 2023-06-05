from abc import ABC, abstractmethod


class Logic(ABC):  # 구현 부분
	@abstractmethod	
	def calculate(self, *args):
		raise NotImplementedError


class Machine(ABC): # 기능 부분
	def __init__(self, logic: Logic):
		self.logic = logic
	
	@abstractmethod
	def calculate(self, *args):
		raise NotImplementedError
	
    
class Add(Logic):
	def calculate(self, *args):	
		numbers, *_ = args
		return sum(numbers)


class Computer(Machine):
	def __init__(self, logic: Logic):
		super().__init__(logic)
		self.logic = logic

	def calculate(self, *args):
		return self.logic.calculate(args)

		
add_logic = Add()
computer = Computer(logic=add_logic)
assert computer.calculate(1,2,3,4,5) == 15
