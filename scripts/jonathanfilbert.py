Author: Jonathan Filbert
Language: Python 3
Github: Jonathanfilbert
#Declaring var i
i = 1
#Iterating from 1 - 100
while i <= 100:
    #check whether divisible by 3 & 5
    if i % 15 == 0:
        print("Spiders")
    #Check whether divisible by 5
    elif i % 5 == 0:
        print("Bats")
    #Check whether divisible by 3
    elif i % 3 == 0:
        print("Cats")
    #Print the number
    else:
        print(i)
    i+=1
