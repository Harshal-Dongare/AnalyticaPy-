
# Static Methods

""" Problem: Add a static method to the Car class that returns a 
general description of a car.
"""

# class variables

""" 
Problem: Add a class variable to Car that keeps track of the number
of cars created.
"""
class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand + " !"
    
    def hello(self):
        return f"Car name is {self.__brand} and model is {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
            
    def fuel_type(self):
        return "Electric Charge"
    
ModelS = ElectricCar("Tesla", "Model S", "85kWh")
safari = Car("Tata", "Safari")
Nexon = Car("Tata", "Nexon")

# print(Nexon.general_description())
print(Car.general_description())

print(Car.total_car)

