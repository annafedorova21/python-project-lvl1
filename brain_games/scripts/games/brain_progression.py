#!/usr/bin/env python
from random import randint

from brain_games.scripts.common import game_launcher


def game_description():
    print("What number is missing"
          " in the progression?")


def brain_progression():

    random_number1 = randint(1, 100)
    random_number2 = randint(1, 20)
    random_missing = randint(0, 9)

    random_number = []
    n = 1

    for i in range(10):
        progression_number = random_number1 + (n - 1) * random_number2
        n = n + 1
        random_number.append(progression_number)

    correct_answer = str(random_number[random_missing])
    random_number[random_missing] = '...'
    random_number = " ".join(map(str, random_number))

    return random_number, correct_answer


def main():
    game_launcher(brain_progression, game_description)


if __name__ == '__main__':
    main()
