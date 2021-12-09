#!/usr/bin/env python3
from readings import readings

#readings = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
#print(readings)

count = 0
last_r = readings[0:3]
for r in range(len(readings)):
    new_r = readings[r:r+3]
    if sum(new_r) > sum(last_r):
        print(last_r)
        print(new_r)
        print('-'*20)
        count += 1
    last_r = new_r

print(count)
