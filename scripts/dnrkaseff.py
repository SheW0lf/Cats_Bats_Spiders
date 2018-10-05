"""

Author: DnrkasEFF
Language: Python
Github: https://github.com/DnrkasEFF
"""

def main():
	for i in range(100):
		if i % 3 == 0:
			if i % 5 == 0:
				print("spiders")
			else:
				print("cats")

		elif i % 5 == 0:
			print("bats")

		else:
			print(i)

	return None

if __name__ == "__main__":
	main()