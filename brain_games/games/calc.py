from random import randint, choice
import operator

game_description = "What is the result of the expression?"


def game():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    math_operator, math_operation = choice(operators)
    random_number = f"{random_number1} {math_operator} {random_number2}"

    correct_answer = str(math_operation(random_number1, random_number2))

    return random_number, correct_answer
