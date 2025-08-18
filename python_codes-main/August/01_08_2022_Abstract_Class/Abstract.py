
from abc import ABC, abstractmethod

class Parent(ABC):
    def property(self):
        print("Jameen, Paisa, Car")

    @abstractmethod
    def marry(self):
        pass

class Child(Parent):

    def marry(self):
        print("Deepika")

obj = Child()
obj.property()
obj.marry()
print(dir(ABC))
print(dir(Parent))
print(dir(Child))
print(dir(obj))
