# Author: Witt Allen
# Language: Python 3.6
# Github: https://github.com/Wittionary/

for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print("spiders")
    elif i % 3 == 0:
        print("cats")
    elif i % 5 == 0:
        print("bats")
    else:
        print(str(i))