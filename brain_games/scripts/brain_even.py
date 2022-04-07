#!/usr/bin/env python
from random import randint


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = input('May I have your name?:')
    print('Hello, {}'.format(name))
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")


def even_or_not():
    counter = 0
    while counter < 3:
        random_number = randint(1, 100)
        print(("Question: {}").format(random_number))
        user_answer = input("Your answer: ")

        if random_number % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(.",
                  "Correct answer was '{correct_answer}' ")
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
            counter += 1
        if counter == 3:
            print(("Congratulations, {}!").format(name))


def main():
    welcome_user()
    even_or_not()


if __name__ == '__main__':
    main()
