
# Polymorphism

"""
Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
"""

class Car:
    def __init__(self, brand, model):
        
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand + " !"
    
    def hello(self):
        return f"Car name is {self.__brand} and model is {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
            
    def fuel_type(self):
        return "Electric Charge"
    
electricCar = ElectricCar("Tesla", "Model S", "85kWh")

# print(electricCar.brand) --> No direct access
print(electricCar.get_brand())

# Method
print(electricCar.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())