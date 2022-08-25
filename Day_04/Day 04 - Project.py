# Rock Paper Scissors ASCII Art
import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

computer_choice_id = random.randint(0, 2)
player_choice_id = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if not (0 <= player_choice_id <= 2):
    print("Wrong input. You've lost. Bye :|")
    exit(0)

choice = [Rock, Paper, Scissors]
print(f"\n{choice[player_choice_id]}\n\nComputer chose:\n\n{choice[computer_choice_id]}\n\n")

if computer_choice_id == player_choice_id:
    print("It is a draw.")
elif choice[player_choice_id] == choice[computer_choice_id - 1]:
    print("You lose. :|")
else:
    print("You win! :)")
