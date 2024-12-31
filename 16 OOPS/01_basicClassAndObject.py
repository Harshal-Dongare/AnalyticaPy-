# Basic Class and Object

""" Create a Car class with attributes like brand and model.
Then create an instance of this class.
""" 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
car1 = Car("BMW", "M3")
print(car1.brand)
print(car1.model)

car2 = Car("TATA", "NEXON")
print(car2.brand)
print(car2.model)

