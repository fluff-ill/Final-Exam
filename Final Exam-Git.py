
# Sophia Carahlay
# Final Exam
# Roll a dice

import random
import time

dice = int(input("How many dice do you want to roll? "))
sides = int(input("How many sides do you want the dice to have? "))
sum = input("Do you want to add your dice together? (yes or no): ")
roll = True

while roll:
    amount = 0
    print("Rolling dice...")
    for i in range (dice):
        time.sleep(1)
        number = random.randint(1, sides)
        print("You rolled", number)
        amount = amount + number
    if sum == "yes":
        print amount
    else: 
        time.sleep(0)
    
    roll = input("do you want to roll again? (yes or no): ")
    if roll == "yes":
        dice = int(input("How many dice do you want to roll? " ))
        sides = int(input("How many sides do you want the dice to have? "))
        continue
    else:
        break
    
print ("Thank you for rolling dice")
