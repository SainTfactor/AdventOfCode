#!/usr/bin/env python3
import re
from data import data

def is_part_num(numobj, data):
    for i in range(numobj["row"] - 1, numobj["row"] + 2):
        for j in range(numobj["start"] - 1, numobj["end"] + 1):
            if not data[i][j] in "0123456789.":
                return True
    return False

def numbers_in_row(row_num, row):
    retval = []
    numbers = re.finditer('\d+', row)
    for i in numbers:
        retval.append({
            "value" : i.group(),
            "row" : row_num,
            "start" : i.span()[0],
            "end" : i.span()[1]
        })
    return retval

data2 = [
    "............",
    ".467..114...",
    "....*.......",
    "...35..633..",
    ".......#....",
    ".617*.......",
    "......+.58..",
    "...592......",
    ".......755..",
    "....$.*.....",
    "..664.598...",
    "............"
]

print(data)
all_nums = []
row_index = 0
for i in data:
    found_nums = numbers_in_row(row_index, i)
    if len(found_nums) > 0:
        all_nums += found_nums
    row_index += 1

val = 0
for i in all_nums:
    if not is_part_num(i, data):
        print(i)
    else:
        val += int(i["value"])
print(val)


# --------------------- Part 2 --------------------- #

def populate_gears(numobj, data, gears):
    for i in range(numobj["row"] - 1, numobj["row"] + 2):
        for j in range(numobj["start"] - 1, numobj["end"] + 1):
            if data[i][j] == '*':
                gears["{},{}".format(i,j)].append(numobj)

gears = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '*':
            gears["{},{}".format(i,j)] = []

for i in all_nums:
    populate_gears(i, data, gears)

val = 0
for i in gears:
    if len(gears[i]) == 2:
        val += int(gears[i][0]["value"]) * int(gears[i][1]["value"])
print(val)
            
