from random import randint
import sys

def run_guess(guess, answer):
    if not isinstance(guess, int):
        raise ValueError("Guess must be a valid integer")

    if not 1 <= guess <= 10:
        print('hey bozo, I said 1~10')
        return

    if guess == answer:
        print('you are a genius!')
        return True
    return False

# generate a number 1~10
answer = randint(1, 10)

# input from user?
# check that input is a number 1~10
if __name__ == "__main__":
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue