
# Sophia Carahlay
# Final Exam
# Roll a dice

import random


roll = True

while roll:
    print("Rolling dice...")
    print("You rolled", random.randint(1, 6))
    roll = input("do you want to roll again? (yes or no): ")
    if roll == "yes":
        continue
    else:
        break
