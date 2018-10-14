# Author: Rashmi Bidanta
# Language: Python3
# Github: https://github.com/rbidanta

'''
Function takes in a number and prints:
"spiders" if the number is divisible by both 3 and 5
"bats" if the number is divisible by 5
"cats" id the number is divisibe by 3
the number otherwise
'''
def catsBatsSpiders(number):

    if number%15 == 0:
        print("spiders")
    elif number%5 == 0:
        print("bats")
    elif number%3 == 0:
        print("cats")
    else:
        print(number)

'''
Executing the Program Here
'''
for num in range(1,101):
    catsBatsSpiders(num)


