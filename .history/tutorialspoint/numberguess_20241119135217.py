# This is our first number guessing game

import random

# Defining variables

n = random.randint(1, 99)
guess = int(input("Enter an integer from 1 to 99: "))

# Do a loop

while n != guess:
    print
    if guess < n:
        print("Your guess is low")