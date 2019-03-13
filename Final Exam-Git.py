
# Sophia Carahlay
# Final Exam
# Roll a dice

"""
This is a Dice Rolling Simulator
Jacob and I both worked on this and Juan helped fix some stuff
This was made for my CSSE Exam
"""

import random
import time


def roll_dice(x):
    # asks the user what the dice does (how many sides and rolls)
    dice = int(input("How many dice do you want to roll? "))
    sides = int(input("How many sides do you want the dice to have? "))

    # asks the user what they want to do with the dice
    sum = input("Do you want to add your dice together? (yes or no): ")
    average = input("Do you want to average your dice roll? (yes or no): ")

    # rolls dice
    roll = True
    while roll:
        amount = 0
        print('\n', "Rolling dice...")

        # rolls the number of dice they chose
        for i in range(dice):

            # time sleep so if they chose a large number it doesn't all come out at once or crash
            time.sleep(x)

            # rolls the dice by chosing a random number between 1 and how many sides the dice has
            number = random.randint(1, sides)
            print("You rolled", number)

            # adds the rolls for the sum
            amount = amount + number

        # prints the sum if the asked for it
        if sum == "yes":
            print("sum: ", amount)

        # prints the average if they asked for it
        if average == "yes":
            # the average is the sum divided by the rolls
            sumav = amount/(float(dice))
            print("average: ", sumav)
        
        # asks user if they want to roll again
        roll = input("do you want to roll again? (yes or no): ")

        if roll == "yes":

            # if they answer yes it will ask the questions again
            print('\n')
            dice = int(input("How many dice do you want to roll? "))
            sides = int(input("How many sides do you want the dice to have? "))
            sum = input("Do you want to add your dice together? (yes or no): ")
            average = input("Do you want to average your dice roll? (yes or no): ")
            continue
        else:
            break
    
    # if they don't chose to roll again it will thank the user
    print('\n', "Thank you for rolling dice")


# runs the function
roll_dice(1)
