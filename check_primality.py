# Ask user for number and determine whether the number is prime or not


def is_prime(number):
    for num in range(2, number):
        if (number % num) == 0:
            print('Not Prime')
            break
        else:
            print('Is Prime')
            break


user_input = int(input('Please enter a number to check if it is prime: '))
is_prime(user_input)
