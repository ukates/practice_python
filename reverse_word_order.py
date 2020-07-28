user_input = input("Please enter a long string with multiple words: ")


def reverse_order(user_string):
    print(" ".join(user_string.split()[::-1]))


reverse_order(user_input)
