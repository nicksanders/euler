#!/usr/bin/python


def word_score(word):
    return sum([ord(char) - 96 for char in word.lower()])

words = []
with open("../data/p042.txt") as f:
    words = f.read().strip(' \t\n\r"').split('","')

result = 0
t_nums = []

for n in range(1, 25):
    t_nums.append(int(0.5 * n * (n + 1)))

for word in words:
    score = word_score(word)
    if score in t_nums:
        result += 1

print(result)
