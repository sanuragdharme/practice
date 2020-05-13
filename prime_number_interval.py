# Print all prime numbers between two numbers


def generate_prime_number(num1, num2):
    if not num1.isdigit() or not num2.isdigit():
        print("Please enter number.")
        return

    num1 = int(num1)
    num2 = int(num2)

    # If larger number is entered first
    if num1 > num2:
        num1, num2 = num2, num1

    while num1 < num2:
        flag = 0
        for i in range(2, int(num1/2)):
            if num1 % i == 0:
                flag = 1
                break

        if flag == 0:
            print(num1, end=" ")

        num1 += 1


enter_num1 = input("Enter 1st Number: ")
enter_num2 = input("Enter 2nd Number: ")
generate_prime_number(enter_num1, enter_num2)
