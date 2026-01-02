# Hangman Game
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
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
  |   |
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
      |
      |
      |
      |
=========''']

# Display a welcome message for the user
print('''
=========================
Welcome to Hangman!
=========================
''')

# Radnomly choose a word from a predefined list
lives = 6
random_words = ["python", "java", "kotlin", "javascript","banana"]
chosen_word = random.choice(random_words)
placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    # User guesses a letter
    user_guess = input("Guess a letter: ").lower()
    # Empty string to store the guessed letters
    display = ""
    # Check if the user guessed letter is in the randomly chosen word
    # Iterate through each letter in the chosen word
    for letter in chosen_word:
        if letter == user_guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if user_guess not in chosen_word:
        lives -= 1
        print(f"You guessed wrong! You have {lives} lives remaining.")
        if lives == 0:
            game_over = True
            print("********************YOU LOSE SUCKER!******************")

    # Check if the user has guessed all letters in the word
    if "_" not in display:
        game_over = True
        print("********************YOU WIN!********************")

    print(stages[lives])

