#!/usr/bin/python

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
# 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


def factor(n):
    f = 1
    for x in range(1, n + 1):
        f *= x
    return f

remain = 1000000 - 1
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
limit = 10
permNum = ''

for i in range(1, 10):
    f = factor(10 - i)
    j = int(remain / f)
    remain = remain % f
    permNum += str(nums[j])
    nums.pop(j)
    if remain == 0:
        break

for i in nums:
    permNum += str(i)

print(permNum)
