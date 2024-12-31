
# Encapsulation

""" 
Problem: Modify the Car class to encapsulate the brand attribute 
making it private, and provide a getter method for it.
"""
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand + " !"
    
    def hello(self):
        return f"Car name is {self.__brand} and model is {self.model}"
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
            
    
    
electricCar = ElectricCar("Tesla", "Model S", "85kWh")

# print(electricCar.brand) --> No direct access
print(electricCar.get_brand())