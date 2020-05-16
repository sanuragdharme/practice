# Types of Arguments
# 1. Formal Arguments :- def add(a, b)
# 2. Actual Arguments :- add(3, 4)


def person(name, location, age=18):
    print(f"Name: {name}, age: {age} and location: {location}")


#   a. Position - In this we can pass argument in any order
print("Position: ")
person(age=23, name="John", location="Canada")

#   b. Keyword - In this we are using keyword (Formal Arguments)
print("Keyword: ")
person(name="John", location="Canada", age=23)

#   c. Default - Means Formal Argument will have default value so that it will become optional in Actual Argument.
#                Default argument will always be declared in the last
print("Default: ")
person("John", "Canada")

#   d. Variable Length - To pass multiple Actual Argument


def addition(*num):
    total = 0
    for i in num:
        total += i
    print("Variable Length: ", total)


addition(5, 6, 34, 78)
print("")

#       i. Keyworded Variable Length Arguments - To pass multiple data with the help of keyword


def person(name, **kwargs): # ** to accept multiple keyword data
    print(name)
    for key, value in kwargs.items():
        print(key, ":", value)


print("Keyworded Variable Length Arguments: ")
person("Moran", age=23, birthplace="Pune", workplace="Pune")
print("")

# Use Global variable inside function

a = 10


def check_global():
    a = 9
    b = globals()['a']
    globals()['a'] = 20
    print(f"Values of a:{a} and b:{b}")
    print(f"Updated value of Global variable a:{globals()['a']}")


check_global()
print("The Value of a:{}".format(a))

# Pass list as argument in function

count_list = [10, 34, 23, 6, 45, 26, 37, 87, 56, 90, 76]


def count(c_list):
    even = 0
    odd = 0

    for i in c_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


even_count, odd_count = count(count_list)
print("The Count of Even:{} and Odd:{}".format(even_count, odd_count))
