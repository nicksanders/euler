#!/usr/bin/python


def split_num(n):
    nums = []
    while n > 0:
        x = n % 10
        n = n // 10
        nums.append(x)
    return nums[::-1]


def join_nums(nums):
    r = 0
    m = 1
    for n in nums[::-1]:
        r += n * m
        m *= 10
    return r


def prime_sieve(limit=125000):
    if limit % 2 != 0:
        limit += 1
    sieve = [True] * limit
    sieve[0], sieve[1] = [False] * 2
    for ind, val in enumerate(sieve):
        if val is True:
            sieve[ind * 2::ind] = [False] * (((limit - 1) // ind) - 1)
    return sieve


def is_all_prime(n):
    nums = split_num(n)
    for i in range(1, len(nums)):
        if sieve[join_nums(nums[i:])] is False:
            return False
    for i in range(-1, 0 - len(nums), -1):
        if sieve[join_nums(nums[:i])] is False:
            return False
    return True

result = []
sieve = prime_sieve(1000000)
primes = [i for i, v in enumerate(sieve) if v is True]

for n in primes:
    if n > 9 and is_all_prime(n):
        result.append(n)

print(sum(result))
