from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError
    

class Word:
    def bad_word(self):
        print("fuck it")


class Speak(Command):
    def __init__(self, word):
        self.word = word
    
    def execute(self):
        self.word.bad_word()


class Person:
    def __init__(self, command):
        self.command = command

    def do_homework(self):
        self.command.execute()


command = Speak(word=Word())
person = Person(command=command)
person.do_homework()
