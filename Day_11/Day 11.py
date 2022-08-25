import os
import random

cards_list = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

logo = '''
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"'''


def shuffle_card():
    return random.choice(list(cards_list.items()))


def calc_scores(p_cards, c_cards):
    p_score, c_score = 0, 0
    p_aces, c_aces = 0, 0
    for item in p_cards:
        p_score += item[1]
        if item[0] == "A":
            p_aces += 1
    for item in c_cards:
        c_score += item[1]
        if item[0] == "A":
            c_aces += 1

    for i in range(0, p_aces):
        if p_score > 21:
            p_score -= 10
    for i in range(0, c_aces):
        if c_score > 21:
            c_score -= 10

    return p_score, c_score


def prompt_retry(player_cards, computer_cards, player_score, computer_score):
    retry = input(
        f"\nPlayer cards: {player_cards}\nComputer cards: {computer_cards}\n\nPlayer score: {player_score}\nComputer "
        f"score: {computer_score}\n\nWould you like to play again? (Y/n): ")
    return retry


def check_player_busted(player_score):
    if player_score > 21:
        print("\nBusted! You've gone more than 21 :(")
        return True
    else:
        return False


def check_computer_busted(computer_score):
    if computer_score > 21:
        print("\nBusted! Computer has gone more than 21 and you have won! :)")
        return True
    else:
        return False


def play():
    os.system('cls')
    print(logo)
    print("Welcome to Python Blackjack!")

    player_cards = []
    computer_cards = []

    is_player_blackjack = False
    is_computer_blackjack = False
    is_anyone_busted = False
    computer_score, player_score = 0, 0

    for i in range(0, 2):
        player_cards.append(shuffle_card())
        computer_cards.append(shuffle_card())

    while not is_anyone_busted:
        player_score, computer_score = calc_scores(player_cards, computer_cards)
        print(f"\nPlayer cards: {player_cards}\nComputer cards: [{computer_cards[0]}, ('X', X)]")
        print(f"\nPlayer score: {player_score}\nComputer score: {computer_cards[0][1]} + X\n")
        is_anyone_busted = check_player_busted(player_score)
        if is_anyone_busted or player_score == 21:
            break
        to_shuffle = input("\nWould you like to take another card? (Y/n): ")
        if to_shuffle.lower() == 'y':
            player_cards.append(shuffle_card())
        else:
            break

    while not is_anyone_busted and computer_score < 17:
        computer_cards.append(shuffle_card())
        player_score, computer_score = calc_scores(player_cards, computer_cards)
        is_anyone_busted = check_computer_busted(computer_score)
        if is_anyone_busted or computer_score == 21:
            break

    if not is_anyone_busted:
        if player_score == computer_score and player_score != 21:
            print("\nIt is a Draw!")
        elif player_score > computer_score:
            print("\nCongratulation! You have won!")
        elif player_score < computer_score:
            print("\nSorry :| You have lost :(")

        if computer_score == 21 and len(computer_cards) == 2:
            is_computer_blackjack = True
        if player_score == 21 and len(player_cards) == 2:
            is_player_blackjack = True

        if is_computer_blackjack:
            print("Blackjack! Computer has won :(")
        elif is_player_blackjack:
            print("Blackjack! You have won :)")

    play_again = prompt_retry(player_cards, computer_cards, player_score, computer_score)
    if play_again.lower() == 'y':
        play()
    else:
        print("\nGood to see you using our Python Blackjack. Have a nice day!\n")
        exit(0)


play()
