# If the reversed integer is equal to the integer entered by user then, that number is a palindrome if not that
# number is not a palindrome.


def check_palindrome(num):
    if not num.isdigit():
        print("Please enter number.")
        return

    if num == num[::-1]:
        print("{} is palindrome".format(num))
    else:
        print("{} is not palindrome".format(num))


check_palindrome(input("Enter Number: "))
