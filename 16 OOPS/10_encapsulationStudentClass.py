class Student:
    # Class variables
    __numberOfStudents = 0
    __schoolName = "MAPS"
    def __init__(self, name, rollNo, marks):
        self.name = name
        self.rollNo = rollNo
        self.__marks = marks
        self.numberOfStudents = Student.__numberOfStudents + 1
        Student.__numberOfStudents += 1

    # getter method for marks
    def get_marks(self):
        return self.__marks

    # setter method for marks
    def set_marks(self, newMarks, passCode):
        if self.__auth(passCode):    # Security feature
            self.__marks = newMarks
        else:
            return "Bhag yaha se!"

    # Method to know total number of students in a school
    @staticmethod
    def get_numberOfStudent():
        return Student.__numberOfStudents

    def get_schoolName(self):
        return Student.__schoolName

    # Method to set school name
    @staticmethod
    def set_schoolName(newName, passCode):
        if passCode == "0000":
            Student.__schoolName = newName
        else:
            return "Tu phir aa gaya murkh!"

    def __auth(self, passCode):
        return True if passCode == "0000" else False

    def study(self):
        print(f"I am {self.name} and I am studying.")

    def play(self):
        print("Done with study. Now it is time to go out and play.")

# Two students
s1 = Student("Harsh", 1, 95)
s2 = Student("Praju", 2, 98)

# Marks for s1 and s2
print(s1.get_marks())
print(s2.get_marks())

# Change marks of student 1 with passcode
s1.set_marks(89, "0000")

# Get total number of students
print(Student.get_numberOfStudent())

# Change the school name
Student.set_schoolName("MH", "0000")







  
