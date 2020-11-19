from factorization import *

def fact():
    print("Hello!")

    while True:
        while True:
            try:
                num = int(input("Please enter a positive number higher than 1: "))

            except:
                print("Please enter a number!")

            else:
                if num > 1:
                    break
                else:
                    print("Please re-read the statement!")
                    continue

        factorization(num)

        re_do = input("Do you want to try with another number? (Y)es or (N)o: ")
        if re_do.lower()[0] == "y":
            continue

        else:
            print("Bye!")
            break

if __name__ == '__main__':
    fact()
