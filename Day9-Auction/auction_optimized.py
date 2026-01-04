from art import logo
import os
print(logo)

# Defining a function to find the highest bidder from the bids_dict dictionary
def find_highest_bidder(bids_dict):
    for bids in bids_dict: # for loop to iterate through each bid in the dictionary
        highest_bidder = 0 # variable to keep track of the highest bid found; initalized to 0
        winner = "" # variable to store the name of the highest bidder; initialized to an empty string
        bid_amount = bids_dict[bids] # retrieves the bid amount for the current bidder
        if bid_amount > highest_bidder: # compares the current bid amount with the highest bid found so far
            highest_bidder = bid_amount # updates the highest bid if the current bid is greater
            winner = bids # updates the winner to the current bidder's name
    os.system('clear') # clears the console for better readability
    print(f"The winner is {winner} with a bid of ${highest_bidder}!")

# Empty dictonary established to store the bids     
bids_dict = {}
should_continue = True

# This is the main bidding loop - if the user types 'yes' for more bidders, then the program will continue to run until 'no' is typed   
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