chai = "Masala Chai"

# Access first character
print(chai[0])

# ---------------------------------------------------------------

# Extract "Masala" word using slicing
sliced_chai = chai[0:6]
print(sliced_chai)

num_list = "0123456789"
print(num_list[3:])     # Starting index
print(num_list[:7])     # End index
print(num_list[0::2])   # Step 


# ---------------------------------------------------------------

# String methods
name = "    Harshal    "
address = "Manpada, Thane, Maharashtra"

print(chai.lower())
print(chai.upper())
print(chai.title())
print(chai.capitalize())

print(name.strip())     # Remove leading and trailing spaces
print(name.rstrip())    # Remove trailing spaces
print(name.lstrip())    # Remove leading spaces

print(address.replace("Manpada", "New York"))     # Replace word in string


# ---------------------------------------------------------------

# Split method divide string based on delimiter and convert to list 
names = "Prajakta, Harshal, Chetan, Riya, Harsh"
print(names.split(", "))

# ---------------------------------------------------------------

# find method returns index of first occurrence of substring
# returns -1 if not found
# find() method is case sensitive
print("Harsh present at index",names.find("Harsh"))

# ---------------------------------------------------------------

# count() method returns number of occurrences of substring
print(f"Harsh present {names.count("Harsh")} times.")

# ---------------------------------------------------------------

# String formatting using format() method
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai."

print(order.format(quantity, chai_type))


# ---------------------------------------------------------------

# Joins list of strings using join() method

places = ["New York", "London", "Paris"]
print(" ".join(places))

# ---------------------------------------------------------------

# print each character of string
str1 = "Lovo"
count = 0

for char in str1:
  print(char, end=" ")
  if count == (len(str1) - 1):
    print()
  count += 1  
    
  

# ---------------------------------------------------------------

# escape characters
chai3 = "He said, \"Masala chai is awesome\""

print(chai3)