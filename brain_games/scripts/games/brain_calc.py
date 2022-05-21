#!/usr/bin/env python
import operator
from random import randint, choice

from brain_games.scripts.common import game_launcher


def game_description():
    print("What is the result of the expression?")


def calc():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    op, ch = choice(operators)
    random_number = (f"{random_number1} {op} {random_number2}")

    correct_answer = str(ch(random_number1, random_number2))

    return random_number, correct_answer


def main():
    game_launcher(calc, game_description)


if __name__ == '__main__':
    main()
