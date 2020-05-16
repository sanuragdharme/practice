# There are 3 types of Methods in class
#


class Student:
    # Class Variable
    school_name = "We Care, We Here"

    # Special Method
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance Method - When we are passing "self" means it is Instance method
    def average_marks(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Class Method - When we fetch Class variable
    @classmethod
    def get_school(cls):
        return cls.school_name

    # Static Method - When are passing no argument
    @staticmethod
    def info_class():        print("Welcome to Static Method")


S1 = Student(34, 23, 56)
S2 = Student(45, 67, 65)

print("The Average of marks: ", S1.average_marks())
print("The Average of marks: ", S2.average_marks())

print(f"The School name is {Student.get_school()}")
Student.info_class()
