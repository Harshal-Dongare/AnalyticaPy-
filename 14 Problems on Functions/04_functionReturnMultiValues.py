# Function returning multiple values

# Write a function that returns both the area and circumference of a circle given its radius

import math

def circle_stats(radius):
    areaOfCir = math.pi * (radius ** 2)
    circumference = 2 * (math.pi) * radius    
    return round(areaOfCir, 2), round(circumference, 2)

ans = circle_stats(4.5)
print("Area of a circle: ",ans[0])
print("Circumference of a circle: ",ans[1])
