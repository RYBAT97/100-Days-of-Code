import random
import os

# Artwork
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
             'coyote crow deer dog donkey duck eagle ferret fox frog goat '
             'goose hawk lion lizard llama mole monkey moose mouse mule newt '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra ').split()

# TODO 1
chosen_word = random.choice(word_list)
chosen_word_puzzle = ""
for item in chosen_word:
    chosen_word_puzzle += "_"
print("Hint: Chosen word is '" + chosen_word + "'")
chosen_word_puzzle = list(chosen_word_puzzle)
history = list()

i = 0
while i < 6:
    # os.system("cls")
    print(HANGMANPICS[i])
    print("Current Guess: " + str(chosen_word_puzzle))

    # TODO 2
    guess = input("\nGuess a letter: ").lower()
    os.system("cls")
    if guess not in history:
        history.append(guess)
    else:
        print("Input already used.")
        continue
    j = 0

    # TODO 3
    if guess in chosen_word.lower():
        print("Correct input.")
        for letter in chosen_word.lower():
            # print(f"j == {j}")
            if guess == letter:
                chosen_word_puzzle[j] = list(chosen_word)[j]
            j += 1
    if guess not in chosen_word.lower():
        i += 1
        print("Wrong input.")
        # print(f"i == {i}")
    if "_" not in chosen_word_puzzle:
        print("You've won! :)")
        print(HANGMANPICS[i])
        exit()

if i == 6:
    print("Sorry, you've lost :(")
    print(HANGMANPICS[i])
