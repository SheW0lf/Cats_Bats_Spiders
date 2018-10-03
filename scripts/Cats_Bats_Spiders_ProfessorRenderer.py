# Author: Professor Renderer
# Language: Python
# Github: https://github.com/Renderer-RCT2

x = 0


for x in range(1, 100):
    if x % 3 is 0 and x % 5 is 0:
        print("spiders")
    elif x % 3 is 0:
        print("cats")
    elif x % 5 is 0:
        print("bats")
    else:
        print(str(x))
