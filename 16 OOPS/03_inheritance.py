
# Inheritance

# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def hello(self):
        return f"Car name is {self.brand} and model is {self.model}"
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
            
    
    
electricCar = ElectricCar("Tesla", "Model S", "85kWh")

print(electricCar.brand)
print(electricCar.model)
print(electricCar.battery_size)
print(electricCar.hello())
    