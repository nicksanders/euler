#!/usr/bin/python


def route_num(cube_size):
    l = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            l[j] = l[j] + l[j - 1]
        l[i] = 2 * l[i - 1]
        print(l[i])
    return l[cube_size - 1]


print(route_num(20))
