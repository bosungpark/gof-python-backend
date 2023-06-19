from abc import ABCMeta, abstractmethod


class Animal(metaclass = ABCMeta):
    @abstractmethod
    def bark(self):
        pass


class Dog(Animal):
    def bark(self):
        print("dog bark!!")


class Cat(Animal):
    def bark(self):
        print("cat bark!!")



class AnimalFactory(object):
    def make_sound(self, animal: Animal):
        return animal.bark()


animal_factory = AnimalFactory()

dog = Dog()
animal_factory.make_sound(animal=dog)
