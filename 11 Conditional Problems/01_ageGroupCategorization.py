
# Program 1: Age group categorization
age = int(input("Enter the age: "))

if age >= 60:
  print("Senior Citizen")
elif 20 <= age < 60:
  print("Adult")
elif 13 <= age < 20:
  print("Teenager")
else:
  print("Child")
