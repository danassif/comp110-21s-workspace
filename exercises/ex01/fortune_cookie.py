"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730329922"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

x: int = randint(1, 4)

if x == 1:
    print("A golden egg of opportunity will fall into your lap this month.")
else:
    if x == 2:
        print("All your hard work will soon pay off.")
    else:
        if x == 3:
            print("Everywhere you chose to go, friendly faces will greet you.")
        else:
            print("Resting well is as important as working hard.")

print("Now, go spread positive vibes!")