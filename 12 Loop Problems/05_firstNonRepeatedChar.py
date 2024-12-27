# Given a string, ind the first non repeated character

text = "Success".lower()

for char in text:
    if text.count(char) == 1:
        print("First non-repeated char is:",char)
        break


