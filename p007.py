#!/usr/bin/python


def nth_prime(n, limit=125000):
    if limit % 2 != 0:
        limit += 1
    primes = [True] * limit
    primes[0], primes[1] = [None] * 2
    cnt = 0
    for ind, val in enumerate(primes):
        if val is True:
            # sieve out non-primes by multiples of known primes
            primes[ind * 2::ind] = [False] * (((limit - 1) // ind) - 1)
            cnt += 1
        if cnt == n:
            return ind
    return False


print(nth_prime(10001))
