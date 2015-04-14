#!/usr/bin/python


def num_divisors(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    return cnt

num = 1

while True:
    prod = sum(range(1, num + 1))
    t = num_divisors(prod)
    if t >= 500:
        break
    print(prod, t)
    num += 1

print(prod)
