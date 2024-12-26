tea_types = ("Black", "Green", "Oolong")

print(tea_types)

# index based access
print(tea_types[1])

# negative indexing
print("Negative indexing", tea_types[-3])

# slicing
print(tea_types[1:])

# Tuples does not support item assignment
# tea_types[0] = "Herbal"   -> Error

# len() function
print("Length of tea_types", len(tea_types))

more_tea = ("Herbal", "Earl Grey")

# Concatenation
all_tea = tea_types + more_tea
print("All teas: ", all_tea)

# Check if an element is in the tuple
if "Herbal" in all_tea:
  print("Herbal tea is in the list")