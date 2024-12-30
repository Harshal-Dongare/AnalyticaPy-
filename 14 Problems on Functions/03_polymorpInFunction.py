# Polymorphism in function

# Write a function name 'multiply' that multiplies two numbers, but can also accept and multiply strings.


def multiply(val1, val2):
    return val1 * val2

value1 = multiply(4, 5)
value2 = multiply("Harshal", 2)
value3 = multiply(2, "Prajakta")

print(value1)
print(value2)
print(value3)