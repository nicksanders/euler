#!/usr/bin/python

nums = []
with open("../data/p013.txt") as f:
    nums = [int(i) for i in f.read().strip('\n').split('\n')]

print(str(sum(nums))[:10])
