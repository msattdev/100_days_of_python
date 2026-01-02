# Hangman Game
import random

# Display a welcome message for the user
print("Welcome to Hangman!")

# Radnomly choose a word from a predefined list
random_words = ["python", "java", "kotlin", "javascript","banana"]
chosen_word = random.choice(random_words)
print(chosen_word)  # For testing purposes; remove in production

# User guesses a letter
user_guess = input("Guess a letter: ").lower()

# Check if the user guessed letter is in the randomly chosen word
# Iterate through each letter in the chosen word
for letter in chosen_word:
    if letter == user_guess:
        print("Correct!")
    else:
        print("Wrong! Guess again!")


