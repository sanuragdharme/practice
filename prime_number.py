# To check whether the entered number is prime or not
def check_prime_number(num):
    if not num.isdigit():
        print("Please enter number.")
        return

    num = int(num)
    if num <= 1:
        print("Enter number greater than 1")
        return

    for i in range(2, num):
        if num % i == 0:
            print("Number is not prime")
            return

    print("Number is prime")


check_prime_number(input("Enter Number: "))
