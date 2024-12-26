# Grade Calculator

marks = int(input("Enter marks: "))

if marks >= 101:
    print("Please verify your grade again.")
    exit()

if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks <= 89:
    print("Grade B")
elif 70 <= marks <= 79:
    print("Grade C")
elif 60 <= marks <= 69:
    print("Grade D")
else:
    print("Grade F")