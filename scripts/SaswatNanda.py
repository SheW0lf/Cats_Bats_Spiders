""""
Author: Saswat Nanda
Language: Python
Github: https://github.com/saswat01
"""
for i in range(1,101):
	if i%3==0:
		print("Cats")
	elif i%5 == 0:
		print("Bats")
	elif i%3==0 and i%5==0:
		print("Cats and Bats")
	else:
		print(i)
