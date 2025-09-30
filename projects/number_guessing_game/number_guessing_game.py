from art import logo
import random

def guess_a_number():
    x = int(input("Please guess a number between 1-100\n"))
    return x

def the_game():
    print(logo)
    random_number = random.choice(range(0, 101))
    print(random_number) # to be deleted
    game_over = False

    difficulty_choice = input("Choose the difficulty 'easy' or 'hard\n").lower()

    if difficulty_choice == "easy":
        lives = 9
    else:
        lives = 4

    player_guess = guess_a_number()

    if player_guess == random_number:
        print(f"Your guess {player_guess} is correct!")
        return game_over

    while not player_guess == random_number:
        if lives == 0:
            print(20 *"\n")
            print("You ran out of guesses!")
            return game_over

        elif player_guess > random_number:
            print(f"Too high!\n You have {lives} guesses left!")
            lives -= 1
            player_guess = guess_a_number()

        elif player_guess < random_number:
            print(f"Too low\n You have {lives} guesses left!")
            lives -= 1
            player_guess = guess_a_number()
    else:
        print(f"Your guess {player_guess} is correct!")


while input("Do you want to play a game? 'y' or 'n'\n") == "y":
    game_over = True
    print(30 * "\n")
    the_game()
else:
    print(30 * "\n")
    print(logo)
    print("Thanks for playing!")
    game_over = True
