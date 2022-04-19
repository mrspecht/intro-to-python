# Classes

class Person:
    def greetings(self, name):                                                  # 'self' is used to represent the instance of a class. By
        print(f"Hello {name}")                                                  # using the 'self' keyword we access the attributes and
                                                                                # methods of the class

me = Person()                                                                   # Every method call associated with an instance automatically
me.greetings("Andre")                                                           # passes 'self', which is a reference to the instance itself
