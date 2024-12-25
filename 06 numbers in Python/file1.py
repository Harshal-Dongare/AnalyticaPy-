x = 2
y = 3
z = 4

print("Addition", x + y)  # Addition
print("Subtraction", x - y)  # Subtraction
print("Multiplication",y * y)  # Multiplication
print("Division",x / y)  # Division
print("Modulus",x % y)  # Modulus
print("Exponent",z ** y)  # Exponent

# Always use parentheses while performing arithmetic operations
print((x + y) * z)

# Not as per industry standards
print(x + y * z)   

# Perform operation of same data type
print(4.5 + 8.9)

# Not as per industry standards
print(4.5 + 8)

# Operators overloading
print('Harshal' + ' Dongare')
print('Harshal ' * 3)


# repr() returns a string representation of an object mainly used
# for debugging purpose.
print(repr('chai'), repr(4.5), repr([1, 2, 3]))  

print(str('chai'), str())
print('chai')

# ----------------------------------------------------------------

# Comparison Operators
# Returns True or False
print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x > y)  # Greater than
print(x < y)  # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to


# Both are same 
print (x < y < z)     # Shorthand for (x < y) and (y < z)
print (x < y and y < z)


# ----------------------------------------------------------------

import math

# math.floor()
# math.ceil()
# math.trunc() : Removes the decimal part and returns the integer part

print("Floor Method : ",math.floor(4.5))
print("Floor Method : ",math.floor(-4.2))
print("Ceil Method :", math.ceil(4.5))
print("Ceil Method :", math.ceil(-4.2))
print("Trunc Method :", math.trunc(4.5))

# ----------------------------------------------------------------

# Complex numbers
complexNum = 3 + 4j
print(complexNum * 4)

# ----------------------------------------------------------------

# binary, Octal and Hexadecimal
print("Octal number: ", 0o10)  
print("Hexadecimal number: " ,0x10)  
print("Binary number: ", 0b1000)


# Conversion from decimal to binary, octal and hexadecimal
print(bin(10))
print(oct(10))
print(hex(10))


# ----------------------------------------------------------------

import random

# .random() returns a random number between 0 and 1
print("Random number:", random.random())

# .randint() returns a random number
print("Random number between 1 and 10:", random.randint(1, 10))

# .choice() returns a random item from a list
print("Random choice: ", random.choice([1, 2, 3]) )

# .shuffle() shuffles a list : changes the original list
shuffledList = ["Harsh", "Praju", "Priya"]
random.shuffle(shuffledList)
print(shuffledList)

# ----------------------------------------------------------------

from decimal import Decimal

print("Without Decimal module: ", 0.1 + 0.1 + 0.1 - 0.3)

result = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print("Using Decimal module: ", result)


# ----------------------------------------------------------------

setOne = {1, 2, 3, 4}

# intersection
print(setOne & {3, 4, 5})

# union
print(setOne | {3, 4, 5})