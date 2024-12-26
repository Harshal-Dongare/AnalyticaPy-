# Leap Year Checker

year = 2024

if (year % 400) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year")