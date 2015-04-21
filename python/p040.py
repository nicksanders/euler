#!/usr/bin/python

from common import split_num

d = [0]
n = 1

while len(d) <= 1000000:
    d.extend(split_num(n))
    n += 1

m = 1
result = 1
for i in range(1, 8):
    result *= d[m]
    m *= 10

print(result)
