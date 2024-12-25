tea_variety = ["Black", "Green", "Oolong", "White"]

print(tea_variety)

# Index based access
print(tea_variety[0], tea_variety[1])

# Negative indexing
print(tea_variety[-2])

# Slicing
print(tea_variety[1:3])

# Element Insertion at a specific index
tea_variety[0] = "Herbal"
print(tea_variety)

# Element insertion in place of multiple indexes
tea_variety[1:3] = ["Hot", "Black"]
print(tea_variety)

tea_variety = ["Black", "Green", "Oolong", "White"]

# Looping through list
for tea in tea_variety:
  print(tea, end=" ")
  
# Check if an element is in the list using `in` keyword
if "White" in tea_variety:
  print("\nWhite tea is in the list")
  
# append() method : add an element to the end of the list
tea_variety.append("Herbal")
print("List after append: ", tea_variety)

# insert() method : add an element at a specific index
tea_variety.insert(1, "Milk")
print("List after insert: ", tea_variety)

# pop() method : remove an element from the end of the lis
removedElement = tea_variety.pop()
print("Removed element: ", removedElement)

# pop(a) method : remove an element from a specific index
removedElement2 = tea_variety.pop(0)
print("Removed element: ", removedElement2)

# remove() method : remove an element from the list
tea_variety.remove("Green")
print("List after removing Green: ", tea_variety)

# copy() method : create a copy of the list
tea_variety_copy = tea_variety.copy()
print("Copied list using copy(): ", tea_variety_copy)

tea_variety_copy[1:1] = ["Hot", "Black"]
print("Copied list after insert: ", tea_variety_copy)
print("Original list does not change: ", tea_variety)


# List comprehension
squared_nums = [x**2 for x in range(10)]
print("List Comprehension: ", squared_nums)