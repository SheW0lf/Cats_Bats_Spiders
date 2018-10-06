"""
Author: Iain Mclaughlan
Language: Python 3
Github: https://github.com/Darthmazgar
"""

size = 100
bat = "Bats"
cat = "Cats"
spiders = "Spiders"
for i in range(1, size+1):
    if i % 3 == 0 and i % 5 == 0:
        print(spiders)
    elif i % 3 == 0:
        print(cat)
    elif i % 5 == 0:
        print(bat)
    else:
        print(i)
