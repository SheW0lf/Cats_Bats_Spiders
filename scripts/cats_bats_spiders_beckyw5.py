"""
Author: Becky Wilson
Language: Python
Github: beckyw5
"""
import random


number = random.randint(1, 100)

if number % 15 == 0:
    print("spiders")
elif number % 5 == 0:
    print("bats")
elif number % 3 == 0:
   print("cats")
else:
    print(number, "is not a cat, or bat, or spider")
