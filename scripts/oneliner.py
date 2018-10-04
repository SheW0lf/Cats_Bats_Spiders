"""
  Author: Yannick Le Roux
  Language: Python
  Github: https://github.com/YannickLeRoux
"""

for i in range(1, 101): print("spider"*(i%15==0) or "cats"*(i%3==0)or "bats"*(i%5==0) or str(i))