import random
import string

pass_length = int(input('How long would you like your password to be? : '))


def password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(length))


print(password(pass_length))
