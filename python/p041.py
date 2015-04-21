#!/usr/bin/python

from common import split_num, prime_sieve


result = 0
sieve = prime_sieve(87654321)

for i in range(2, len(sieve)):
    if sieve[i] == False:
        continue
    nums = split_num(i)
    if sorted(nums) == list(range(1, len(nums) + 1)):
        if i > result:
            result = i

print(result)
