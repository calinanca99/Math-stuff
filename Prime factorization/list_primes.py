from is_prime import *

def list_primes(n):
    primes = []
    for j in range(2,n+1):
        if is_prime(j) == True:
            primes.append(j)

    return primes
