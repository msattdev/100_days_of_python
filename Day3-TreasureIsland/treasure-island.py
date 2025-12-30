# Treasure Island Project
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/____/___
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure!")
print("You're at a crossroad. Where do you want to go?")
choice1 = input("      Type \"Left\" or \"Right\" \n").lower()

if choice1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake")
    choice2 = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if choice2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        choice3 = input("One red, one yellow, and one blue. Which color do you choose?\n").lower()
        if choice3 == "yellow":
            print("Congrats! You chose the right door and YOU WIN!")
        elif choice3 == "red":
            print("You chose the wrong door and fell into a pit of lava. GAME OVER!")
        else:
            print("You chose the wrong door and fell into a barrel of acid. GAME OVER!")
    else:
        print("You were eaten by a freshwater shark. GAME OVER!")
else:
    print("You fell into a hole. Game Over!")