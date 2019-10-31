"""
  Author: Sarthak Thakur
  Language:Python 3
  Github: https://github.com/sarthak247
"""

lst = ['spiders' if x%15==0 else 'cats' if x%3==0 else 'bats' if x%5==0 else x for x in range(1,101)]

for i in lst:
    print(i)