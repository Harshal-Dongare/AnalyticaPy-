# Function with *args

""" 
Write a function that takes variable number of arguments 
and returns their sum 
"""

def sumOfNum(*args):
    return sum(args)


ans1 = sumOfNum(1, 2, 3, 4, 5)
ans2 = sumOfNum(63, 2, 4)

print(ans1)
print(ans2)