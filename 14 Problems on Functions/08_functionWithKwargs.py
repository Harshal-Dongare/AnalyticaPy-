# Function with **kwargs

"""
Create a function that accepts any number of keyward arguments
and prints them in the format key:value
"""

def randomFun(**kwargs):
    for key, value in kwargs.items():
        print(key, " : ", value)
    
randomFun(power="lazer", name="Shaktiman", enemy="Dr. Jackaal" )