"""
Author: Becky Wilson
Language: Python
Github: beckyw5
"""
import random


class CatsBatsSpiders():

    def cats_bats_spiders_checker(self, number):
        if number % 15 == 0:
            print("spiders")
            return "spiders"
        elif number % 5 == 0:
            print("bats")
            return "bats"
        elif number % 3 == 0:
           print("cats")
           return "cats"
        else:
            print(number, "is not a cat, or bat, or spider")
            return "none"

if __name__ == '__main__':
    number = random.randint(1, 100)
    CatsBatsSpiders().cats_bats_spiders_checker(number)
