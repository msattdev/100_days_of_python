from art import logo

print(logo)

def calculate(first_number, second_number, operation_picked):
    if operation_picked == "+":
        return first_number + second_number
    elif operation_picked == "-":
        return first_number - second_number
    elif operation_picked == "*":
        return first_number * second_number
    elif operation_picked == "/":
        return first_number / second_number
    else:
        print("Error: Invalid Operation!")

first_number = float(input("What is the first number?: "))
print("+\n-\n*\n/")
operation_picked = input("Pick an operation: ")
second_number = float(input("What is the next number?: "))
should_continue = True

while should_continue:
    result = calculate(first_number, second_number, operation_picked)
    print(f"{first_number} {operation_picked} {second_number} = {result}")
    next_step = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
