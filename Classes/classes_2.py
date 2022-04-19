# Classes

class Person:
    def __init__(self, name, job, age=18):                                      # __init__ is the class constructor
        self.name = name                                                        # Constructors are used to initialize the object’s state
        self.job = job
        self.age = age                                                          # Methods with two '__' are called dunder methods

    def info(self):
        print(f"Name: {self.name}")
        print(f"Job: {self.job}")
        print(f"Age: {self.age}")


employee_1 = Person("John Doe", "Programmer", age=27)
employee_1.info()

employee_2 = Person("Mary Helen", "DB manager")
employee_2.info()

print(employee_1.name)
