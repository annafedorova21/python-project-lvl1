#!/usr/bin/env python
from random import randint

from brain_games.common import welcome_user, task_description
from brain_games.common import ask_question
from brain_games.common import get_answer, print_correct, print_error, print_congratulations


def brain_progression(name):
    counter = 0
    while counter < 3:
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 20)
        random_missing = randint(0, 9)

        progression = []
        n = 1

        for i in range(10):
            progression_number = random_number1 + (n - 1) * random_number2
            n = n + 1
            progression.append(progression_number)

        correct_answer = progression[random_missing]
        progression[random_missing] = '...'
        progression = " ".join(map(str, progression))
        ask_question(progression)

        user_answer = int(get_answer())

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
    task_description("What number is missing"
                     "in the progression?")
    brain_progression(name)


if __name__ == '__main__':
    main()
