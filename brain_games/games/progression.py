from random import randint


game_description = "What number is missing"\
                   " in the progression?"


def game():

    random_number1 = randint(1, 100)
    random_number2 = randint(1, 20)
    random_missing = randint(0, 9)

    random_number = []
    n = 1

    for i in range(10):
        progression_number = random_number1 + (n - 1) * random_number2
        n = n + 1
        random_number.append(progression_number)

    correct_answer = str(random_number[random_missing])
    random_number[random_missing] = '..'
    random_number = " ".join(map(str, random_number))

    return random_number, correct_answer
