# Reverse a string


# Method 1: Reverse method
name = "Harshal"
# convert to list of characters
name_array = list(name)
# reverse the list
name_array.reverse()
# Converts reversed list of characters into string
reverseString = "".join(name_array)
print("Reversed String using reverse() method:",reverseString)

# ------------------------------------------------------------------


# Method 2: using for loop
input_str = "Harshal"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str

print("Reversed String using for loop:", reversed_str)


# ------------------------------------------------------------------


# Method 3: using negative indexing

input_name = "Prajakta"

rev = input_name[::-1]

print("Reverse string using negative indexing:", rev)