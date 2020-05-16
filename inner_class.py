class Student:

    def __init__(self, name, rollno):
        self.__name = name
        self.__rollno = rollno
        self.__lap = self.Laptop()

    def show(self):
        print("Name: {} and Roll No: {}".format(self.__name, self.__rollno))

    def get_laptop(self):
        return self.__lap

    class Laptop:

        def __init__(self):
            self.__brand = "Apple"
            self.__cpu = 'i7'
            self.__ram = 8

        def show(self):
            print(f"Laptop details: {self.__brand}, {self.__cpu} and {self.__ram}")


s1 = Student("Kevin", 33)
s1.show()
s1.get_laptop().show()
