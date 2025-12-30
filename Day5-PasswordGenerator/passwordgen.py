# Password Generator
import random

print("Welcome to the PyPassword Generator!")
letter_length = int(input("How many letter would like in your password?\n"))
symbol_length = int(input("How many symbols would like in your password?\n"))
number_length = int(input("How many numbers would like in your password?\n"))

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!#$%&()*+'
numbers = '0123456789'

password_letters = [random.choice(letters) for x in range(letter_length)]
password_symbols = [random.choice(symbols) for x in range(symbol_length)]
password_numbers = [random.choice(numbers) for x in range(number_length)]

password_list = password_letters + password_symbols + password_numbers
random.shuffle(password_list)
password = ''.join(password_list)
print(f"Your password is: {password}")