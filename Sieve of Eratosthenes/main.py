import sys
from sieve_erat import erat
from get_num import get_num
from get_choice import get_choice

def soe():
    print("I can give a list of primes up to and including n, where n>1.\n")
    while True:
        num = get_num()
        nums = erat(num)

        print("\nThe numbers are: {}".format(nums))

        while True:
            choice = get_choice()

            if choice == 1:
                print("\nThere are {} primes\n".format(len(nums)))
                continue

            elif choice == 2:
                print("\nTheir sum is {}\n".format(sum(nums)))
                continue

            elif choice == 3:
                break

            elif choice == 4:
                sys.exit()

if __name__ == '__main__':
    soe()
