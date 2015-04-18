#!/usr/bin/python

total = 0
fact = 1
for x in range(1, 101):
    fact *= x

while fact > 0:
    x = fact % 10
    total += x
    fact = (fact - x) // 10

# total = sum([int(i) for i in str(fact)])

print(int(total))
