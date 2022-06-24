from random import randint


game_description = "Find the greatest common divisor "\
                   "of given numbers."


def greatest_common_divider(random_number1, random_number2):

    if random_number1 > random_number2:
        n = 0
        list = [random_number1, random_number2]

    else:
        n = 0
        list = [random_number2, random_number1]

    while list[len(list) - 1] > 0:
        x = list[n] % list[n + 1]
        list.append(x)
        n += 1

    return str(list[len(list) - 2])


def game():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    random_number = f"{random_number1} {random_number2}"

    correct_answer = greatest_common_divider(random_number1, random_number2)

    return random_number, correct_answer
