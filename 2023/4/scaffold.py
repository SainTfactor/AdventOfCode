#!/usr/bin/env python3
from data import data

data2 = [
    [[41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]],
    [[13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]],
    [[1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]],
    [[41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]],
    [[87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]],
    [[31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11]]
]

print(data)

val = 0
for card in data:
    count = len([i for i in card[1] if i in card[0]])
    if count > 0:
        val += 2**(count - 1)
print(val)

# --------------------- Part 2 --------------------- #

cards = {}
for i in range(1, len(data) + 1):
    cards[i] = 1

cur_card = 1
for card in data:
    count = len([i for i in card[1] if i in card[0]])
    for _ in range(cards[cur_card]):
        for i in range(1, count + 1):
            cards[cur_card + i] += 1
    cur_card += 1

val = 0
for i in cards:
    val += cards[i]
print(val)


