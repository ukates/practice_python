# generate a number ask user to guess number for every digit the user guesses correctly in correct place they have 'cow'
# Every digit correct but in wrong place they have a bull, continue until user guesses


import random


def play_game():
    secret_number = [random.randint(0, 9) for i in range(4)]

    user_guess = ''

    print('This is the cows and bulls game!')
    print('\nGuess the four digit number,\neach correct number in correct place is a cow,\n' +
          'each correct number in wrong place is a bull.')

    while user_guess != 'quit':
        user_guess = list(map(int, input('\nPlease guess the 4 digit number: ')))

        cows = 0
        bulls = 0

        if user_guess == secret_number:
            print('You Win!, you guessed %s and the correct number was %s' % (user_guess, secret_number))
            break

        for i in range(4):
            if secret_number[i] == user_guess[i]:
                cows += 1
                if bulls >= 0:
                    bulls -= 1
            elif secret_number[i] in set(user_guess):
                bulls += 1

        print('You got %d cows and %d bulls' % (cows, bulls))
        print(secret_number)
        user_guess = input('Press enter to try again, or type quit to end: ')


if __name__ == "__main__":
    play_game()
