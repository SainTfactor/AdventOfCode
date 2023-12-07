#!/usr/bin/env python3
from math import ceil, floor


data = [[7,9], [15,40], [30,200]] # test data
data = [[56,334],[71,1135],[79,1350],[99,2430]] # real data

def race_option_count(race_time, previous_best):
    retval = -((race_time+1)%2)
    up = ceil(race_time/2)
    down = floor(race_time/2)
    while True:
        if up * down <= previous_best:
            break
        #print("--- {}, {}".format(up, down))
        retval += 2
        up += 1
        down -= 1
    return retval

printy = 1
for datum in data:
    x = race_option_count(*datum)
    printy *= x
print(printy)

# --------------------- Part 2 --------------------- #

data = [71530,940200]
data = [56717999,334113513502430]

print(race_option_count(*data))

