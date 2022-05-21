#!/usr/bin/env python
from random import randint

from brain_games.scripts.common import game_launcher


def game_description():
    print("Answer 'yes' if the number is prime, otherwise answer 'no'.")


def brain_prime():

    random_number = randint(1, 100)

    for i in range(2, random_number):

        if random_number % i == 0:
            correct_answer = "no"
            break
        else:
            correct_answer = "yes"

    return random_number, correct_answer


def main():
    game_launcher(brain_prime, game_description)


if __name__ == '__main__':
    main()
