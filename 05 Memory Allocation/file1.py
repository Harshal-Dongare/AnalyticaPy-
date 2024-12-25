
# In this case value of a and b will be same as both are pointing to same object. So each time we change the value of a, it will change the value of b.
a = [1, 2, 3]
b = a

print("Value of a and b before change: ", a, b)

a[0] = 33

print("Value of a and b after change: ", a, b)

# ---------------------------------------------------------------
# ---------------------------------------------------------------

# In this case value of a and b will be different as both are pointing to different objects. So each time we change the value of a, it will not change the value of b.

list_one = [4, 5, 6]
list_two = list_one

print("Value of list_one and list_two before change: ", list_one, list_two)

# This [4, 5, 6] looks same as list_one but it is pointing to different object.
list_two = [4, 5, 6]

# changing list_one value will not change list_two value.
list_one[0] = 44

print("Value of list_one and list_two after change: ", list_one, list_two)

# ---------------------------------------------------------------
# ---------------------------------------------------------------

"""
== : compare values of two objects
is : compare address of two objects
"""

m = [1, 2, 3]
n = [1, 2, 3]

print(m == n)       # True
print(m is n)       # False

