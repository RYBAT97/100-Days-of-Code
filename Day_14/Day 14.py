import os
import random

import Data

logo = Data.logo
data = Data.data
vs = Data.vs
score = 0

# Last stat: 0 for first round, 1 for last answer correct, 2 for last answer wrong
last_stat = 0

A = random.choice(data)
data.remove(A)

while len(data) > 0:
    os.system('cls')
    print(logo)
    if last_stat == 1:
        print(f"You're right! Current score: {score}")
    elif last_stat == 2:
        print(f"Sorry, that's wrong. Final score: {score}")
        exit()
    B = random.choice(data)
    data.remove(B)
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if A['follower_count'] > B['follower_count']:
        winner = 'a'
    else:
        winner = 'b'

    if winner == choice:
        last_stat = 1
        score += 1
        A = B
    else:
        last_stat = 2

os.system('cls')
print(f"Congratulations! You've won the game withe high score of {score}!")
