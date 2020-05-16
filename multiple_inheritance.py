class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show_name(self):
        print(self.__name)

    def show_age(self):
        print(self.__age)


class Salary:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        print(self.__salary)


class Database(Employee, Salary):

    def __init__(self, name, age, salary):
        Employee.__init__(self, name, age)
        Salary.__init__(self, salary)

    def extra_def(self):
        print("This is extra in Database")


emp1 = Database("Mohit", 29, 100000)
emp1.show_name()
emp1.show_age()
emp1.get_salary()
emp1.extra_def()