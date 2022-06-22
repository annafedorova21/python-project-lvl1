def game_launcher(game_name, game_description):
    print("Welcome to the Brain Games!")
    name = input('May I have your name?:')
    print('Hello, {}'.format(name))
    game_description()

    counter = 0
    while counter < 3:
        random_number, correct_answer = game_name()

        print(("Question: {}").format(random_number))
        user_answer = input("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
            counter += 1
        if counter == 3:
            print(f"Congratulations, {name}!")
