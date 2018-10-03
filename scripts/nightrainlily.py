"""
AUTHOR: Amaya Lim
LANGUAGE: Python
GITHUB: https://github.com/nightrainlily
"""

for num in range(1, 100):
	if num % 3 == 0 and num % 5 == 0:
		x = "spiders"
	elif num % 3 == 0:
		x = "cats"
	elif num % 5 == 0:
		x = "bats"
	else:
		x = num
print(x)