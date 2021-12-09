#!/usr/bin/env python3
from directions import directions

#directions = [("F", 5), ("D",  5), ("F", 8), ("U",  3), ("D",  8), ("F", 2)]
#print(directions)

aim=0
x=0
y=0
for direction in directions:
    if direction[0] == "F":
        x+=direction[1]
        y+=direction[1]*aim
    if direction[0] == "U":
        aim-=direction[1]
    if direction[0] == "D":
        aim+=direction[1]

print(x*y)
