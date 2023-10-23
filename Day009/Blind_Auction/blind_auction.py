import os
from art import logo


def adding_bidder():
    print("Welcome to the secret auction progra.")
    auctioner_name = input("What's your name?\n")
    auctiones_bid = int(input("Insert your bid:\n"))
    auctioners_dict[auctioner_name] = auctiones_bid


def find_winner():
    winner = ""
    bid = 0
    for auctioner, auctiones_bid in auctioners_dict.items():
        if auctioners_dict[auctioner] > bid:
            bid = auctiones_bid
            winner = auctioner
    print(f"The winner is {winner} with a bid of ${bid}")


auctioners_dict = {}
os.system("clear")
print(logo)
while True:
    adding_bidder()
    more_bidders = input("Are there any other bidder? Type 'yes' or 'no'. \n")
    if more_bidders.lower() == "yes":
        os.system("clear")
    else:
        os.system("clear")
        find_winner()
        break
