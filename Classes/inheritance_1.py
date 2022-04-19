# Inheritance

class Mammal:
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs')
        super().__init__('Dog')                                                 # super() returns a proxy object (temporary object of
                                                                                # the superclass) that allows us to access methods of
                                                                                # the base class
dog = Dog()
