#!/usr/bin/python

ways = 1

target = 200
coin_sizes = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0] * (target + 1)
ways[0] = 1

for i in range(0, len(coin_sizes)):
    for j in range(coin_sizes[i], (target + 1)):
        ways[j] += ways[j - coin_sizes[i]]

print(ways[-1])
