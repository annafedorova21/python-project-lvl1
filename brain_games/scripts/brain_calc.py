#!/usr/bin/env python
import operator
from random import randint, choice

from brain_games.common import welcome_user, task_description, ask_question
from brain_games.common import get_answer
from brain_games.common import print_correct, print_error, print_congratulations


def calc(name):
    counter = 0
    while counter < 3:
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 100)
        oprs = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
        op, ch = choice(oprs)
        random_number = (f"{random_number1} {op} {random_number2}")
        ask_question(random_number)
        user_answer = int(get_answer())

        correct_answer = ch(random_number1, random_number2)

        if user_answer != correct_answer:
            print_error(name, user_answer, correct_answer)
            break
        else:
            print_correct()
            counter += 1
        if counter == 3:
            print_congratulations(name)


def main():
    name = welcome_user()
    task_description("What is the result of the expression?")
    calc(name)


if __name__ == '__main__':
    main()
