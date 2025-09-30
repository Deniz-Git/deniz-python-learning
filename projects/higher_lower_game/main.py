from game_data import data
from art import logo
from art import vs
import random

"""THERE IS A BUG THAT EATS THE DATA :D NEED TO FIX IT AND MAKE THE GAME LOOK PRETTIER AND WE ARE DONE!"""

# TODO GAME if user guesses correct score += 1 if not game_over = True
    # TODO Print score
        # TODO Do you want to play again_

# TODO Random picker function to be called as follow:
    # TODO Start of the game we start with 2nd slot randomly selected
    # TODO If correct answer is in slot 1 refresh 2
    # TODO IF CORRECT ANSWER is in slot 2 move it to slot 1 and insert new random to slot 2

# TODO player guess
# TODO Compare = True or Fale


# TODO MAIN: ACCESS DICTIONARY AND CALL STUFF
# TODO MAIN: PRESENT SLOTS WITH DESCRIPTIONS

# TODO HOW CAN I RANDOMLY REMOVE AN ITEM FROM A LIST








def play_the_game():
    temp_list = []
    temp_list.extend(data)


    score = 0
    game_over = False
    check_answer = False

    while not game_over:
        def random_from_list():
            x = random.choice(temp_list)
            temp_list.remove(x)
            return x



        if check_answer == False:
            first_slot = random_from_list()
            second_slot = random_from_list()

        if check_answer == True:
            first_slot = correct_answer
            second_slot = random_from_list()



        print("\n" * 30)
        print(logo)

        print(f"Compare A: {first_slot['name']} a {first_slot['description']} from {first_slot['country']} {first_slot['follower_count']} ")

        print(vs)

        print(f"Compare B: {second_slot['name']} a {second_slot['description']} from {second_slot['country']} {second_slot['follower_count']}  ")

        guess = str(input("Who has more instagram followers?").lower())

        if guess == "a":
            guess = int(first_slot["follower_count"])
            o_guess = int(second_slot["follower_count"])
            if guess > o_guess:
                print(f"Correct! {guess} has {o_guess} million followers")
                score += 1
                check_answer = True
                correct_answer = first_slot

            else:
                print(f"Unfortunately {first_slot["name"]} has {o_guess - guess} millions more followers.")
                print(f"Your score: {score}")
                game_over = True


        elif guess == "b":
            guess = int(second_slot["follower_count"])
            o_guess = int(first_slot["follower_count"])
            if guess > o_guess:
                print(f"Correct! {guess} has {o_guess} million followers")
                score += 1
                check_answer = True
                correct_answer = second_slot
            else:
                print(f"Unfortunately {first_slot["name"]} has {o_guess - guess} millions more followers.")
                print(f"Your score: {score}")
                game_over = True

while input("Do you want to play? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_the_game()
