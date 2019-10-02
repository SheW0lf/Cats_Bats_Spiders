# Author: Deepak Chauhan
# Language: Python3
# Github: https://github.com/royaleagle73

for n in range(1,101):
	if n%3==0 and n%5==0:
		print("spiders")
	elif n%3==0:
		print("cats")
	elif n%5==0:
		print("bats")
	else:
		print(n)
