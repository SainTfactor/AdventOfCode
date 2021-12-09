#!/usr/bin/env python3
from data import data

#data = [16,1,2,0,4,2,7,1,2,14]
#print(data)

my_index=-1
shortest = 100000000000000000000000000
for i in range(max(data)):
    runner = 0
    for datum in data:
        #runner += abs(datum-i)
        distance = abs(datum-i)
        runner += (distance*(distance+1))/2
    if runner < shortest:
        my_index=i
        shortest = runner
print(my_index)
print(shortest)
