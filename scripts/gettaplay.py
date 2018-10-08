'''
Author: MAG
Language: Python
Github: https://github.com/gettaplay
'''
for i in range(1,100+1):
    if i%3 == 0 and i%5 == 0:
        print('spiders')
    elif i%3 == 0:
        print('cats')
    elif i%5 == 0:
        print('bats')
    else:
        print(i)