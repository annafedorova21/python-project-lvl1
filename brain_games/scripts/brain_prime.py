#!/usr/bin/env python
from random import randint

from brain_games.common import welcome_user, task_description
from brain_games.common import ask_question, get_answer
from brain_games.common import print_correct, print_error, print_congratulations


def brain_prime(name):
    counter = 0
    while counter < 3:
        random_number = randint(1, 100)

        correct_answer = "yes"

        for i in range(2, random_number):
            if random_number % i == 0:
                correct_answer = "no"

        ask_question(random_number)
        user_answer = get_answer()

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
    task_description("Answer 'yes' if given number is prime."
                     " Otherwise answer 'no'.")
    brain_prime(name)


if __name__ == '__main__':
    main()
