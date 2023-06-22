from abc import ABC, abstractmethod
from typing import List


class People(ABC):
    @abstractmethod
    def say_name(self) -> None:
        raise NotImplementedError("You should implement this!")


class Peoples(People):
    def __init__(self) -> None:
        self.peoples: List[People] = []

    def say_name(self) -> None:
        for people in self.peoples:
            people.say_name()

    def add(self, people: People) -> None:
        self.peoples.append(people)

    def remove(self, people: People) -> None:
        self.peoples.remove(people)


class A(People):
    def say_name(self) -> None:
        print(f"Hi, My name is {self.__class__.__name__}")


class B(People):
    def say_name(self) -> None:
        print(f"Hi, My name is {self.__class__.__name__}")


peoples: Peoples = Peoples()
peoples.add(people=A())
peoples.add(people=B())

peoples.say_name()