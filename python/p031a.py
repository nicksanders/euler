#!/usr/bin/python


ways = 1

for a in range(0, 3):
    for b in range(0, 5):
        for c in range(0, 11):
            for d in range(0, 21):
                for e in range(0, 41):
                    for f in range(0, 101):
                        acc = (100 * a) + (50 * b) + (20 * c) + (10 * d) + (5 * e) + (2 * f)
                        if acc <= 200:
                            ways += 1

print(ways)
