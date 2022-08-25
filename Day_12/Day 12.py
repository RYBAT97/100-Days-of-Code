import os
import random


def play_number_guessing():
    os.system('cls')
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Please choose the difficulty -> Type 'Easy' or 'Hard': ")
    choices_count = 0

    if difficulty.lower() == 'easy':
        choices_count = 10
    else:
        choices_count = 5

    the_chosen_one = random.randint(1, 101)
    print(f"\nHint: The chosen one is {the_chosen_one}.\n")

    while choices_count > 0:
        print(f"\nYou have {choices_count} attempts remaining to guess the number.")
        player_choice = int(input("Make a guess: "))
        print(f"\nPlayer choice: {player_choice}, Chose one: {the_chosen_one}\n")
        if player_choice > the_chosen_one:
            print("Too high!")
        elif player_choice < the_chosen_one:
            print("Too low!")
        elif player_choice == the_chosen_one:
            print("Jackpot!")
            break

        print("Guess again...")
        choices_count -= 1

    if choices_count == 0:
        print("You've run out of attempts. Sorry, you've lost :|\n")
    else:
        print("You were able to guess the number. Good job, you've won :)\n")

    retry = input("Would you like to play again? (Y/n)\n")
    if retry.lower() == 'y':
        play_number_guessing()
    else:
        print("Have a nice day!")


play_number_guessing()
