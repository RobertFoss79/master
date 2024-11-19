# This is a rolling dice game
import random

# Defining variables

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dice...")
    print("The values are...")
    print(random.randint(min, max))

    roll_again =input("Roll the dice again? ")
else:
    print("Thank you for playing this wonderful game")
