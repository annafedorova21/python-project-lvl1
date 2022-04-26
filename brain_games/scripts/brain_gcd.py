#!/usr/bin/env python
from random import randint

from brain_games.common import welcome_user, task_description, ask_question
from brain_games.common import get_answer
from brain_games.common import print_correct, print_error, print_congratulations


def greatest_common_divider(name):
    counter = 0
    while counter < 3:
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 100)
        random_number = (f"{random_number1} {random_number2}")

        ask_question(random_number)
        user_answer = int(get_answer())

        if random_number1 > random_number1:
            n = 0
            list = [random_number1, random_number2]

        else:
            n = 0
            list = [random_number2, random_number1]

        while list[len(list) - 1] > 0:
            x = list[n] % list[n+1]
            list.append(x)
            n += 1
        
        correct_answer = list[len(list) - 2]

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
    task_description("Find the greatest common divisor "
                     "of given numbers.")
    greatest_common_divider(name)


if __name__ == '__main__':
    main()
