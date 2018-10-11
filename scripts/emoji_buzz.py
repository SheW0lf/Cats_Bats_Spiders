"""
Author: Sabrina
Language: Python
Github: https://github.com/sabrinakoehler
"""

"""
This program prints the numbers from 1 to 100, but for numbers that are multiples of 3,
prints 'cats' and the cat emoji instead of the number,
for numbers that are multiples of 5 prints 'bats' and the bat emoji instead of the number,
and for numbers that are multiples of both 3 and 5 prints 'spiders' and the spider emoji.
"""

for i in range(1, 100+1):
    if i%3 == 0 and i%5 == 0:
        print('spiders', u"\U0001F577")
    elif i%3 == 0:
        print(u"\U0001F431", 'cats')
    elif i%5 == 0:
        print('bats', 	u"\U0001F987")
    else:
        print(i)
