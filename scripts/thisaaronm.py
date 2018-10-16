#!/usr/bin/env python3

"""
Author: Aaron M
Language: EN-US (or Python...I assumed Python was a given since *.py...)
Github: https://github.com/thisaaronm
"""

def main():
    for i in range(1, 101):
        if i%3 == 0 and i%5 == 0:
            print('spiders')
        elif i%3 == 0:
            print('cats')
        elif i%5 == 0:
            print('bats')
        else:
            print(i)

if __name__ == '__main__':
    main()
