def main():
    print("Are you a Spider or Cat? Please enter answer.")
    s = input("Spider | Cat")
    s = s.lower()
    if (s=="spider"):
        print("Congratulations! You now are a spider. Enjoy spinning the webs!")
    elif(s=="cat"):
        print("Congratulations! You are now a cat. Enjoy the quick reflexes!")
    else:
        print("Not an option. Stop wasting my time.")

if __name__ == "__main__":
    main()

