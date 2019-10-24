#  Author: Bec Braughton
#  Language: Python 2.7.12
#  Github: https://github.com/beckton

#https://github.com/SheW0lf/Cats_Bats_Spiders
#Cats, Bats, and Spiders Hacktoberfest Starter Project
    #Print 1-100
    #for multiples of 3, print 'cats'
    #for multiples of 5, print 'bats'
    #for multiples of 3 & 5, print 'spiders'

num = 0

for i in range(0,100):
    while num < 100:
        num += 1
        if((num % 3) == 0 and (num % 5) != 0):
            print("cats")
 
        elif((num % 3) != 0 and (num % 5) == 0):
            print("bats")
 
        elif((num % 3) == 0 and (num % 5) == 0):
            print("spiders")
 
        elif((num % 3) != 0 and (num % 5) != 0):
            print num
