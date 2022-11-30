"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO:
    """
    answer = random_word()
    # The answer will be replaced by dash.
    dashed = ''
    for i in range(len(answer)):
        dashed += '-'
    print('The word looks like: '+str(dashed))
    print('You have '+str(N_TURNS)+' guesses left.')
    guess = input('Your guess: ')
    new_n_turns = N_TURNS
    # If the number of guess the player has is not zero, this game keep going.
    while new_n_turns != 0:
        guess = guess.upper()  # Case-insensitive.
        new_dashed = ''
        find = False  # Inspect guessing right or wrong.
        if form(guess) == -1:
            print('illegal format.')
        else:
            for j in range(len(answer)):
                if answer[j] == guess:
                    find = True  #有猜到設成True
                    new_dashed += guess
                else:
                    new_dashed += dashed[j]
            dashed = new_dashed
            # This game is over when players answers all the characters correct.
            if '-' not in dashed:
                print('You win!!')
                print('The word was: ' + str(answer))
                break
            if not find:
                # The number of guess the player has will minus when players guess wrong.
                new_n_turns = new_n_turns - 1
                print('There is no '+str(guess)+'\'s in the word.')
                # This game is over when the number of guess the player has is zero.
                if new_n_turns == 0:
                    print('You are completely hung : (')
                    print('The word was: ' + str(answer))
                    break
            else:
                print('You are correct!')
            print('The word looks like ' + str(dashed))
            print('You have '+str(new_n_turns)+' guesses left.')
        guess = input('Your guess: ')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def form(guess):
    # Inspect the format of users' guess.
    formation = guess.isalpha()
    if not formation:
        return -1
    if len(guess) != 1:
        return -1
    return 1


if __name__ == '__main__':
    main()
