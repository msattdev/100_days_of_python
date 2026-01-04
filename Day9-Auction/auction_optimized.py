from art import logo
import os
print(logo)

def find_highest_bidder(bids_dict):
    for bids in bids_dict:
        highest_bidder = 0
        winner = ""
        bid_amount = bids_dict[bids]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bids
    print(f"The winner is {winner} with a bid of ${highest_bidder}!")
        
bids_dict = {}
should_continue = True

while should_continue:
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid amount?: $"))
    bids_dict[name] = bid_amount
    more_bidders = input("Are there anymore bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "no":
        should_continue = False
        find_highest_bidder(bids_dict)
    elif more_bidders == "yes":
        os.system('clear')
        continue