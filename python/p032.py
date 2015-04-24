#!/usr/bin/python

from common import split_num

result = set()

for a in range(2, 100):
    b_start = 123 if a > 9 else 1234
    b_end = 10000 // a + 1
    for b in range(b_start, b_end):
        c = a * b
        nums = set(list(split_num(a)) + list(split_num(b)) + list(split_num(c)))
        if not nums ^ {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            result.add(c)


print(sum(result))
