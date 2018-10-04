#Author: Anish 
#Language: Python
#Github: https://github.com/anish03

for i in range(1,101):
    if i % 3 == 0:
        print 'cats'
    elif i % 5 == 0:
        print 'bats'
    elif i % 3 == 0 and i % 5 == 0:
        print 'spiders'
    else:
        print i
