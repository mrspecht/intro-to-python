# Inheritance

class Parent:
    def message(self):
        print("A message from your parent class")

    def secret_number(self):
        return 4582905


class Child(Parent):
    def message(self):
        super().message()                                                       # Calls the method in the parent class

    def secret(self):
        num = super().secret_number()
        print(f"The secret number is {num}")


c = Child()
c.message()
c.secret()
