#!/usr/bin/env python3

"""
Author: Aditya Krishnakumar
Language: Python3
Github: https://github.com/beingadityak
"""

def main():
    for i in range(1,100):
        if i % 3 is 0:
            if i % 5 is 0:
                print("Spiders")
            print("Cats")
        elif i % 5 is 0:
            print("Bats")
        else:
            print(i)


if __name__ == "__main__":
    main()