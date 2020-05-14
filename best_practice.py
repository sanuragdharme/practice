# 10 Python Tips and Tricks For Writing Better Code
# Credit: Corey Schafer
# Youtube Link: https://youtu.be/C-gEQdGVXbk

######################################################################

# 01. Ternary Conditionals
condition = True

if condition:
    x = 1
else:
    x = 0

print("01. Ternary Conditionals - Before:", x)


x = 1 if condition else 0
print("01. Ternary Conditionals - After:", x)
print("")

######################################################################

# 02. Underscore Placeholders
num1 = 10000000000
num2 = 100000000

total = num1 + num2
print("02. Underscore Placeholders - Before:", total)


num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2
print("02. Underscore Placeholders - After:", f'{total:,}')
print("")

######################################################################

# 03. Context Managers
f = open("text.txt", "r")
file_content = f.read()
f.close()

words = file_content.split(" ")
word_count = len(words)
print("03. Context Managers - Before:", word_count)


with open("text.txt", "r") as file:
    file_content = file.read()

words = file_content.split(" ")
word_count = len(words)
print("03. Context Managers - After:", word_count)
print("")

######################################################################

# 04. Enumerate - To get the index without using incrementer
names = ['Mahesh', 'Mihir', 'Vijay', 'Morris']
index = 0
print("04. Enumerate - Before:")
for name in names:
    print(index, name)
    index += 1


names = ['Mahesh', 'Mihir', 'Vijay', 'Morris']
print("04. Enumerate - After:")
for index, name in enumerate(names, start=1):
    print(index, name)
print("")

######################################################################

# 05. Zip
names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
print("05. Zip - Before:")
for index, name in enumerate(names):
    hero = heroes[index]
    print("{} is actually {}".format(name, hero))

names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
universes = ["Marvel", "DC", "Marvel", "DC"]
print("05. Zip - After:")
for value in zip(names, heroes, universes):
    print(value)

for name, hero, universe in zip(names, heroes, universes):
    print(f"{name} is actually {hero} from {universe}")
print("")

######################################################################

# 06. Unpacking
# a, b, c = (1, 2, 3, 4, 5) # We get an error (ValueError - too many values to unpack)
# print("06. Unpacking - Before:", a)

a, b, c, _, _ = (1, 2, 3, 4, 5)
print("06. Unpacking - After:", a, b, c)

# Here a & b will get 1st two values, d will get last value and c will get remaining all
a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
print("06. Unpacking - After: a({}) b({}) c({}) and d({})".format(a, b, c, d))

# Here a & b will get 1st two values, d will get last value and remaining will get ignored
a, b, *_, d = (1, 2, 3, 4, 5, 6, 7)
print("06. Unpacking - After: a({}) b({}) and d({})".format(a, b, d))

######################################################################

# 07. Setattr/Getattr


class Person:
    pass


person = Person()
person.first = "Peter"
person.last = "Parker"

print("07. Setattr/Getattr - Before: First({}) Last({}) ".format(person.first, person.last))


class Person:
    pass


person = Person()
first_key = "first"
first_name = "Peter"
setattr(person, first_key, first_name)
print("07. Setattr/Getattr - After:", getattr(person, first_key))

person = Person()
person_info = {"first": "Peter", "last": "Parker"}
for key, value in person_info.items():
    setattr(person, key, value)
print("07. Setattr/Getattr - After:", getattr(person, "first"), getattr(person, "last"))

print("07. Setattr/Getattr - After:")
for key in person_info.keys():
    print(getattr(person, key))
######################################################################

# 08. GetPass - Worked properly in terminal
username = input("Username: ")
password = input("Password: ")

print("08. GetPass - Before: Login Successful)")

# to hide the password while typing
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")

print("08. GetPass - After: Login Successful)")


######################################################################

# 09. Python dash m - Worked in terminal

######################################################################

# 10. Help/Dir - Worked in terminal

######################################################################
