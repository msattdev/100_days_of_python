from art import logo
import os
print(logo)

bids = {}
# TODO-1: Ask the user for input
user_name = input("What is your name?: ")
user_bid = int(input("What is your bid?: $"))
# TODO-2: Save data into dictionary {name: price}
bids[user_name] = user_bid
# TODO-3: Whether if new bids need to be added
more_bidders = input("Are there any more bidders? Type 'yes' or 'no'.\n").lower()
while more_bidders == 'yes':
    os.system('clear')
    # If yes, repeat the process
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    bids[user_name] = user_bid
    more_bidders = input("Are there any more bidders? Type 'yes' or 'no'.\n").lower()
# TODO-4: Compare bids in dictionary
highest_bid = 0
winner = ""
for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
# TODO-5: Print the winner
os.system('clear')
print(f"The winner is {winner} with a bid of ${highest_bid}!")