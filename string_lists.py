# Ask user for string and print out whether the string is palindrome


user_string = input('Please enter a word: ').lower()
reversed_string = "".join(reversed(user_string))

print('is palindrome') if user_string == reversed_string else print('not palindrome')

# Alternate

alt_Reversed = user_string[::-1]

print('is palindrome') if user_string == alt_Reversed else print('not palindrome')
