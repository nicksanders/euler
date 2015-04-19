#!/usr/bin/python

num = 1
diag1 = 1
diag2 = 0
step = 2

for i in range(500):
    for s in range(1, 5):
        num += step
        if s % 2 == 0:
            diag1 += num
        else:
            diag2 += num
    step += 2

print(diag1 + diag2)
