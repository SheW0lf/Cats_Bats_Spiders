# Author: Andrea
# Language: R
# Github: https://github.com/kaywinnet

for (number in 1:100)
  {
  if ((number %% 3 == 0) && (number %% 5 != 0))
  {print("cats")}
  else if ((number %% 5 == 0) && (number %% 3 != 0))
  {print("bats")}
  else if((number %% 3 == 0) && (number %% 5 == 0))
  {print("spiders")}
  else
  {print(number)}
  }
