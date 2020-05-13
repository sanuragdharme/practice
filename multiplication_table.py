# To generate multiplication table of a number


def multiplication(num):
    if not num.isdigit():
        print("Please enter number.")
        return

    num = int(num)
    for i in range(1, 11):
        print("{} * {} = {}".format(num, i, num * i))


multiplication(input("Enter Number to generate multiplication table: "))
