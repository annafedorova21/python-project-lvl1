#!/usr/bin/env python

from random import randint

from brain_games.common import welcome_user, task_description, ask_question
from brain_games.common import get_answer
from brain_games.common import print_correct, print_error, print_congratulations


def even_or_not(name):
    counter = 0
    while counter < 3:
        random_number = randint(1, 100)
        ask_question(random_number)
        user_answer = get_answer()
        if random_number % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
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
    task_description("Answer 'yes' if the number is even,"
                     "otherwise answer 'no'.")
    even_or_not(name)


if __name__ == '__main__':
    main()
