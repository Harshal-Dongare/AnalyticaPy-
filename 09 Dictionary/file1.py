chai_types = {"Masala" : "Spicy", "Ginger" : "Zesty", "Green" : "Mild"}

print("chai types: ", chai_types)

# Accessing values using square brackets
print("Masala chai taste: ", chai_types["Masala"])

# Accessing values using get() method
print("Ginger tea taste: ", chai_types.get("Ginger"))

# Change values
chai_types["Green"] = "Fresh"
print("Added chai types: ", chai_types)

# Add new key-value pair
chai_types["Earl Grey"] = "Citrus"
print("Updated chai types: ", chai_types)

# delete a key-value pair
deletedChai = chai_types.pop("Ginger")
print("Deleted Chai using pop(): ",deletedChai)

# deletes key-value pair from memory
del chai_types["Earl Grey"]
print("Deleted chai types using del: ", chai_types)

# Delete a last key-value pair
lastChai = chai_types.popitem()
print("Deleted Chai using popitem(): ",lastChai)

print("-----------------------------------------------")
# ---------------------------------------------------------------


chai_types = {"Masala" : "Spicy", "Ginger" : "Zesty", "Green" : "Mild"}

# Iterating through dictionary
for chai in chai_types:
  # Print keys only
  print("Tea :", chai)
  
for chai, taste in chai_types.items():
  # Print keys and values
  print(chai, ":", taste)
  
for taste in chai_types.values():
  # Print values only
  print("Taste: ", taste)
  
# Check if a key exists using `in` keyword
if "Masala" in chai_types:
  print("Masala is in chai_types")
  
# Length of dictionary
print("Length of a dictioary: ", len(chai_types))
  
# ---------------------------------------------------------------

# Copying a dictionary
chai_types_copy = chai_types.copy()

# Nested dictionary
tea_shop = {
  "chai" : {
    "Masala" : "Spicy",
    "Ginger" : "Zesty"},
  "Tea" : {
    "Green" : "Mild", 
    "Black" : "Strong"}
}
print(tea_shop)

# Accessing nested dictionary
print("Nested dictionary: ", tea_shop["chai"]["Masala"])

# ---------------------------------------------------------------

# Dictionary Comprehension
squared_nums = {x : x**2 for x in range(6)}
print("Dict Comprehension: ", squared_nums)

# Clear all the values
chai_types.clear()
print("Cleared chai_types: ", chai_types)


# ---------------------------------------------------------------

keys = ["Masala", "Ginger", "Green"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)

print(new_dict)