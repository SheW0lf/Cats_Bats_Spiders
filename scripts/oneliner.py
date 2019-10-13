"""
  Author: Yannick Le Roux
  Language: Python
  Github: https://github.com/YannickLeRoux
"""

for i in range(1, 101): 
  print("spider"*(i%15==0) or 
        "cats"*(i%6==0)or
        "bats"*(i%8==0) or
        str(i))
