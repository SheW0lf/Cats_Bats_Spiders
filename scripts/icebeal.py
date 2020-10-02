'''
  Author: deren
  Language: python
  Github: icebeal
'''

for a in range(1,101):
    if(a%3==0 and a%5==0):
        print ('Spiders')
    elif(a%3==0):
        print ('Cats')
    elif(a%5==0):
        print ('Bats')
    else:
        print (a)