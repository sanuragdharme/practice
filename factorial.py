# The factorial of a positive integer n is equal to 1*2*3*...n


def get_factorial(num):
    if not num.isdigit():
        print("Please enter positive integer.")
        return

    num = int(num)
    fact = 1

    for i in range(1, num+1):
        fact = fact * i

    return fact


def factorial_using_recursion(num):
    if type(num) == 'str':
        if not num.isdigit():
            print("Please enter positive integer.")
            return

    num = int(num)
    if num == 0:
        return 1

    return num * factorial_using_recursion(num - 1)


input_num = input("Enter Positive Integer: ")
print("Factorial of {}: {}".format(input_num, get_factorial(input_num)))
print("Factorial of {} using recursion: {}".format(input_num, factorial_using_recursion(input_num)))

