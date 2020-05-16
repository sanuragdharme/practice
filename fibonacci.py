# The Fibonacci sequence is a series where the next term is the sum of previous two terms.
# The first two terms of the Fibonacci sequence is 0 followed by 1


def generate_fibonacci(num):
    if not num.isdigit():
        print("Please enter number.")
        return

    num = int(num)
    num1 = 0
    num2 = 1

    for i in range(1, num + 1):
        print(num1, end=" ")
        fibonacci = num1 + num2
        num1, num2 = num2, fibonacci


def generate_fibonacci_till_num(num):
    if not num.isdigit():
        print("Please enter number.")
        return

    num = int(num)
    num1 = 0
    num2 = 1

    while num:
        print(num1, end=" ")
        if num1 == num:
            break
        fibonacci = num1 + num2
        num1, num2 = num2, fibonacci


generate_fibonacci(input("Enter Number: "))
print("")
generate_fibonacci_till_num(input("Enter Number when you want to stop: "))