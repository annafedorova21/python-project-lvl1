def game_launcher(module):
    print("Welcome to the Brain Games!")
    name = input('May I have your name?:')
    print('Hello, {}'.format(name))
    print(module.game_description)

    number_of_attemps = 3
    for n in range(number_of_attemps):
        random_number, correct_answer = module.game()

        print("Question: {}".format(random_number))
        user_answer = input("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
        if n == 2:
            print(f"Congratulations, {name}!")
