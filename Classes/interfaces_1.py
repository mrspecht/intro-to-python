# Interfaces (abstract classes)
                                                                                # By default, Python does not provide abstract classes
from abc import ABC, abstractmethod                                             # Python comes with a module that provides the base for defining
                                                                                # 'Abstract Base Classes' and that module name is 'ABC'
class Abstract(ABC):
    @abstractmethod                                                             # Decorator to flag an abstract method
    def greetings(self):
        pass


class Concrete(Abstract):
    def greetings(self):
        print("Hello world")


c = Concrete()
c.greetings()
