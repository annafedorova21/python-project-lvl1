from random import randint


def game_description():
    print("Answer 'yes' if the number is prime, otherwise answer 'no'.")


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def brain_prime():

    random_number = randint(2, 100)

    if is_prime(random_number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return random_number, correct_answer
