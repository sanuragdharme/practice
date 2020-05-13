# To check entered character is vowel or not


def check_vowel(char):
    char = char[0]
    vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    if char in vowel_list:
        print("{} is vowel.".format(char))
    else:
        print("{} is consonant.".format(char))


check_vowel(input("Enter character: "))
