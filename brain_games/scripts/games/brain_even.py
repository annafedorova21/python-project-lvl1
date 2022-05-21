#!/usr/bin/env python

from random import randint

from brain_games.scripts.common import game_launcher


def game_description():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")


def even_or_not():
    random_number = randint(1, 100)

    if random_number % 2 == 0:

        correct_answer = "yes"
    else:
        correct_answer = "no"

    return random_number, correct_answer


def main():
    game_launcher(even_or_not, game_description)


if __name__ == '__main__':
    main()
