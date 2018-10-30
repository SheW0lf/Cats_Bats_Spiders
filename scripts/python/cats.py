def find_cats_bats_spiders(num1, num2):
    for num in range(num1, num2):
        if num % 3 and num % 5 == 0:
            print("spiders")
        elif num % 5 == 0:
            print("bats")
        elif num % 3 == 0:
            print("cats")
        else:
            print(num)


find_cats_bats_spiders(1, 100)
