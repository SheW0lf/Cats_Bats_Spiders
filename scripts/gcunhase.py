"""
    Author: Gwena Cunha (Gwenaelle Cunha Sergio)
    Language: Python
    Github: https://github.com/gcunhase

    Write a program that prints the numbers from 1 to 100, but for numbers that are multiples of 3,
     print 'cats' instead of the number, for numbers that are multiples of 5 print 'bats' instead of the number,
     and for numbers that are multiples of both 3 and 5 print 'spiders'.
"""

for i in range(1, 101):
    print_str = i
    if i % 3 == 0 and i % 5 == 0:
        print_str = 'spiders'
    else:
        if i % 3 == 0:
            print_str = 'cats'
        if i % 5 == 0:
            print_str = 'bats'
    print(print_str)
