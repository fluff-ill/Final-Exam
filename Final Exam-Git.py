
# Sophia Carahlay
# Final Exam
# Roll a dice

import random

dice = input("How many dice do you  want to roll?")
roll = True

while roll:
    print("Rolling dice...")
    for i in range (dice):
        print("You rolled", random.randint(1, 6))
    roll = input("do you want to roll again? (yes or no): ")
    if roll == "yes":
        dice = int(input("How many dice do you  want to roll?" ))
        continue
    else:
        break
