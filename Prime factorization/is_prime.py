def is_prime(n):
    if n <= 0:
        return False
    elif n == 1 or n == 2:
        return True
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        else:
            return True
