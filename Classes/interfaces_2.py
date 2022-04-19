# Interfaces (abstract classes)

from abc import ABC, abstractmethod

class Animal(ABC):                                                              # 'Class(ABC)' is the signature of an abstract class
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Eagle(Animal):
    def move(self):
        print("I can fly")


h = Human()
h.move()

s = Snake()
s.move()

e = Eagle()
e.move()
