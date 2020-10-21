# Author: verebecske
#  Language: python3
#  Github: https://github.com/verebecske

class CatsBatsSpiders:
     def __init__(self, min, max):
          self.min = min
          self.max = max
          self.cat = 1
          self.bat = 1
          self.spider = 1

     def cats(self, i: int):  # 3
          if self.cat * 3 == i:
               print('cats')
               self.cat = self.cat + 1
               return True
          return False


     def bats(self, i: int):  # 5
          if self.bat * 5 == i:
               print('bats')
               self.bat = self.bat + 1
               return True
          return False


     def spiders(self, i: int):  # 15
          if self.spider * 15 == i:
               print('spiders')
               self.spider = self.spider + 1
               self.cat = self.cat + 1
               self.bat = self.bat + 1
               return True
          return False

     def catsbats_printer(self):
          for i in range(self.min, self.max+1):
               if not self.spiders(i) and not self.cats(i) and not self.bats(i):
                    print(i)


if __name__ == "__main__":
    min = 1
    max = 100
    catsbats = CatsBatsSpiders(min,max)
    catsbats.catsbats_printer()


