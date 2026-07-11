# Inheritance Example

# Vehicle → Car


class Vehicle:

    def __init__(self,brand):
        self.brand=brand

    def display(self):
        print(self.brand)

class Car(Vehicle):

    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model

    def display(self):
        super().display()
        print(self.model)

car=Car("Toyota","Corolla")

car.display()