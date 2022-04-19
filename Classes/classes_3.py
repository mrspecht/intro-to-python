# Classes

class Calculator:
    intro = "Calculator 1.0"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mult(self):
        return self.x * self.y


calc = Calculator(8, 5)
print(calc.add())
print(calc.sub())
print(calc.mult())

print(calc.intro)

calc.z = 33
print(calc.z)
