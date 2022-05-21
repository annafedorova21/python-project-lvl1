#!/usr/bin/env python
from random import randint

from brain_games.scripts.common import game_launcher


def game_description():
    print("Find the greatest common divisor "
          "of given numbers.")


def greatest_common_divider():

    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    random_number = (f"{random_number1} {random_number2}")

    if random_number1 > random_number1:
        n = 0
        list = [random_number1, random_number2]

    else:
        n = 0
        list = [random_number2, random_number1]

    while list[len(list) - 1] > 0:
        x = list[n] % list[n + 1]
        list.append(x)
        n += 1

    correct_answer = str(list[len(list) - 2])

    return random_number, correct_answer


def main():
    game_launcher(greatest_common_divider, game_description)


if __name__ == '__main__':
    main()
