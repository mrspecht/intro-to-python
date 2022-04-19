# Inheritance

class Vehicle:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine

    def info(self):
        print(self.brand)
        print(self.model)
        print(self.engine)


class Car(Vehicle):
    def __init__(self, brand, model, engine, wheels):
        super().__init__(brand, model, engine)
        self.wheels = wheels

    def info(self):
        print(self.brand)
        print(self.model)
        print(self.engine)
        print(self.wheels)


car = Car("Lamborghini", "Centenario", "Turbo", 4)
car.info()
