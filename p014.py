#!/usr/bin/python

res = 0
max_cnt = 0

for i in range(1, 1000000):
    n = i
    cnt = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        cnt += 1

    if cnt > max_cnt:
        res = i
        max_cnt = cnt

print(res)
