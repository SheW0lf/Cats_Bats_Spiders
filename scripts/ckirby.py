#Author: Chaim Kirby
#Language: python3
#Github: https://github.com/ckirby

# Cats Bats Spiders oneliner implementation (FizzBuzz equivalent)

print(' '.join("Cats"*(i%3==0)+"Bats"*(i%5==0) or str(i) for i in range(1,101)).replace('CatsBats','Spiders'))


