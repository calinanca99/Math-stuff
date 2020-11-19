def get_choice():
    print("\nPlease choose:")
    while True:
        try:
            choice = int(input("1.How many primes?\n2.What's their sum?\n3.Input another number\n4.Quit.\n>>>>>>>>"))

        except:
            print("Please enter a number")

        else:
            if choice == 1 or choice == 2 or choice == 3 or choice == 4:
                return choice
            else:
                print("Please choose between 1, 2, 3 or 4!")
                continue
