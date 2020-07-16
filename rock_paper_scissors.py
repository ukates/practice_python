# Make two player RPS game


def play_game(p1, p2):
    if p1 == p2:
        return 'Game over, its a tie!'
    elif p1 == 'r':
        if p2 == 's':
            return 'Rock wins'
        else:
            return 'Paper wins'
    elif p1 == 's':
        if p2 == 'p':
            return 'Scissors wins'
        else:
            return 'Rock wins'
    elif p1 == 'p':
        if p2 == 'r':
            return 'Paper wins'
        else:
            return 'Scissors wins'


quit = ''
choices = ['r', 'p', 's']

while quit != 'quit':
    player1 = input('Player 1, Please press a key (r = rock, p = paper, s = scissors): ')
    if player1 not in choices:
        player1 = input('**CHOICE INVALID** Please press a key (r = rock, p = paper, s = scissors): ')

    player2 = input('Player 2, Please press a key (r = rock, p = paper, s = scissors): ')
    if player2 not in choices:
        player2 = input('**CHOICE INVALID** Please press a key (r = rock, p = paper, s = scissors): ')

    print(play_game(player1, player2))
    quit = input('Type quit to end, or enter to continue: ')
