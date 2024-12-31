
#  Class Method and Self

# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def hello(self):
        return f"Car name is {self.brand} and model is {self.model}"
        
car1 = Car("Mercedes", "GLS")

print(car1.hello())