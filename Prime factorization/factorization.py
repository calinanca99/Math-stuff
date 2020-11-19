from list_primes import *

def factorization(n):
    jic = n
    factors = []
    primes = list_primes(n)
    while n>1:
        for k in primes:
            if n%k == 0:
                factors.append(k)
                n = n/k
    if len(factors) > 1:
        print("The prime factors are {}.".format(sorted(factors)))

    else:
        print("{} is a prime!".format(jic))
