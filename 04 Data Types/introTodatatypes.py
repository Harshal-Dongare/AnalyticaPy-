# print statement
print(12 + 12)
print(4.5 * 5)
print(4 ** 100)

# Math module
import math
print(math.pi)

# Random module
import random
print(random.randint(1, 10))
print(random.random())
print(random.choice([1, 2, 3, 4, 5]))


# String
username = "chai aur code"
print("Length of username: ", len(username))
print("Index based access: ", username[2])
print(username[-1])     # negative indexing
print(username[0:4])    # slicing/substring
print(dir(username))

# List
myList = [123, "chai", 3.14]
print("List: ", myList)
print(len(myList))
print(myList[0])    # Index based access
print(myList[-1])   # Negative indexing
print(myList[0:2])  # Slicing/substring

# Dictionary
myDict = {"name": "harshal", "age": 20}
print("Dictionary: ", myDict)
print(myDict["name"])

# Tuple
myTuple = (1, 2, 3)
print("My tuple: ", myTuple)
print("First element: ", myTuple[0])
print("Length: ", len(myTuple))