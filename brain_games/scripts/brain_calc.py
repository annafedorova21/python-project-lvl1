#!/usr/bin/env python
import operator
from random import randint, choice

from common.py import welcome_user, task_description, ask_question, get_answer, print_correct, print_error, print_congratulations

def calc(name):
    counter = 0
    while counter < 3:
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 100)
        operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
        op, ch = choice(operators)
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
