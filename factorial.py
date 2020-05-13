# The factorial of a positive integer n is equal to 1*2*3*...n


def get_factorial(num):
    if not num.isdigit():
        print("Please enter positive integer.")
        return

    num = int(num)
    fact = 1

    for i in range(1, num+1):
        fact = fact * i

    print("Factorial of {}: {}".format(num, fact))


get_factorial(input("Enter Positive Integer: "))

