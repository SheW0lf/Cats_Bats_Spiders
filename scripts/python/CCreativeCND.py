#Author: Calu DIngwall
#Language: Python
#GitHub: https://github.com/ccreativecnd

n=0

while n<101:
  s = None
  if n%3 == 0:
    if n%5 == 0:
      s = "Spiders"
    else:
      s = "Cats"
  elif n%5 == 0:
    s = "Bats"
  print(s or n)
  n = n + 1
