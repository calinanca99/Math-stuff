def get_num():
    while True:
        try:
            num = int(input("Please enter a positive number higher than 1: "))

        except:
            print("Please enter a number!")

        else:
            if num > 1:
                return num
            else:
                print("Please re-read the statement!")
                continue
