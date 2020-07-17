# Create random number guessing game for user, tell user high or low

import random


def play_game(guess):
    secret_number = random.randint(1, 10)
    if guess == secret_number:
        print("You have figured out the secret number!")
        pass
    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is too high try again")
        else:
            print("Your guess is too low try again")
        guess = int(input("Please enter your new guess: "))
        if guess == secret_number:
            print("You have figured out the secret number!")


user_guess = int(input("Guess the secret number 1 - 9: "))
play_game(user_guess)
