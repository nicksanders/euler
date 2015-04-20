#!/usr/bin/python


def split_num(n):
    while n > 0:
        x = n % 10
        n = (n - x) // 10
        yield x


def rotate_num(num):
    x = num % 10
    num_digits = len(list(split_num(num)))
    multiplier = (10 ** num_digits) // 10
    for _ in range(num_digits):
        x = num % 10
        num = (x * multiplier) + (num // 10)
        yield num


def prime_sieve(limit=125000):
    if limit % 2 != 0:
        limit += 1
    sieve = [True] * limit
    sieve[0], sieve[1] = [False] * 2
    for ind, val in enumerate(sieve):
        if val is True:
            sieve[ind * 2::ind] = [False] * (((limit - 1) // ind) - 1)
    return sieve

limit = 1000000
result = []
sieve = prime_sieve(limit)
primes = [i for i, v in enumerate(sieve) if v is True]

for prime in primes:
    for n in split_num(prime):
        if (n % 2 == 0 or n == 5):
            sieve[prime] = False

    all_prime = True
    for p in list(rotate_num(prime))[0:-1]:
        if sieve[p] is False:
            all_prime = False
    if all_prime:
        result.append(prime)

print(len(result))
