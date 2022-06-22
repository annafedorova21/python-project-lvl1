from random import randint


def game_description():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")


def even_or_not():
    random_number = randint(1, 100)

    if random_number % 2 == 0:

        correct_answer = "yes"
    else:
        correct_answer = "no"

    return random_number, correct_answer
