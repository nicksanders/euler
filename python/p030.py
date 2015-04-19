#!/usr/bin/python


def split_num(n):
    while n > 0:
        x = n % 10
        n = (n - x) // 10
        yield x


nums = []

for i in range(2, 1000000):
    if sum([x ** 5 for x in split_num(i)]) == i:
        nums.append(i)

print(sum(nums))
