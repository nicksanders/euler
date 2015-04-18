#!/usr/bin/python

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first
# names,  begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is
# the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?


def word_score(word):
    return sum([ord(char) - 96 for char in word.lower()])

words = []
with open("../data/p022.txt") as f:
    words = f.read().strip(' \t\n\r"').split('","')

total = 0
for i, word in enumerate(sorted(words), 1):
    total += i * word_score(word)

print(total)
