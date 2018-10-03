# Author: dumblole
# Language: python 3.6
# Github: https://github.com/dumblole

# python 3.6
for a in range(1, 101):  # range isn't inclusive for the second parameter
    if(a % 5 == 0 and a % 3 == 0):
        print('spiders')
    elif(a % 3 == 0):
        print('cats')
    elif(a % 5 == 0):
        print('bats')
    else:
        print(a)
