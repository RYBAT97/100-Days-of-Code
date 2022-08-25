import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
'''
bidders = []
winner = []
while True:
    os.system("cls")
    print(logo)
    print("Welcome to the Silent Auction Program!")
    name = input("Please enter your name: ")
    bid = input("Please enter the amount you want to bid: $")
    bidders.append({
        "name": name,
        "bid": float(bid)
    })
    more_bids = input("All done! Any more bids? (Y/n)\n")
    if more_bids.lower() == "n":
        break

winner = bidders[0]
total_winners = 0
for i in range(1, len(bidders)):
    if bidders[i]["bid"] > winner["bid"]:
        winner = bidders[i]

os.system("cls")
print(logo)
print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")
