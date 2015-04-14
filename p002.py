#!/usr/bin/python

nums = [1, 2]

while True:
    v = nums[-2] + nums[-1]
    if v < 4000000:
        nums.append(v)
    else:
        break

print(sum([n for n in nums if n % 2 == 0]))
