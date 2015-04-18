#!/usr/bin/python

limit = 1000000
cache = [0] * limit
cache[1] = 1
result = [1, 1]

for i in range(1, limit):
    n, cnt = i, 0
    while n > limit - 1 or cache[n] == 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        cnt += 1

    cache[i] = cache[n] + cnt
    if cache[i] > result[1]:
        result = [i, cache[i]]

print(result)
