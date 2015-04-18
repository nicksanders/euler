#!/usr/bin/python

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if
# this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the
# sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by
# analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant
# numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def proper_divisors(n):
    d = {1}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d |= {i, n // i}
    return d


def get_abundants(max):
    abundants = []
    for i in range(12, max + 1):
        if i < sum(proper_divisors(i)):
            abundants.append(i)
    return abundants

limit = 28123
sieve = [False] * limit

abundants = get_abundants(limit)

for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        if abundants[i] + abundants[j] >= limit:
            break
        sieve[abundants[i] + abundants[j]] = True

print(sum([i for i in range(len(sieve)) if not(sieve[i])]))
