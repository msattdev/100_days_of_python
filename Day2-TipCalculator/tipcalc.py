# Tip Calculator
# Welcome message
print("Welcome to the tip calculator!")
# Ask the user what the total bill is
total_bill = float(input("What was the total bill? $"))
# Ask the user what percentage tip they would like to give
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
# Ask the user how many people will be splitting the bill
split = int(input("How many people to split the bill?"))
# Calculate the total bill per person including tip, stored as a new variable
bill_per_person = total_bill * (1 + tip_percentage / 100) / int(split)

print("Calculating...")
print("-------------------")
print("BEEP BOOP BEEP BOOP")
print("-------------------")
print(f"Each person should pay: ${round(bill_per_person, 2)}")