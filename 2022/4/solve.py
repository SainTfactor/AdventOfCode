#!/usr/bin/env python3
from data import data

#data = [[(2, 4), (6, 8)], [(2, 3), (4, 5)], [(5, 7), (7, 9)], [(2, 8), (3, 7)], [(6, 6), (4, 6)], [(2, 6), (4, 8)]]

out=0
for i in data:
  x1,x2,y1,y2 = i[0][0],i[1][0],i[0][1],i[1][1]
  if (x1 >= x2 and y1 <= y2) or (x1 <= x2 and y1 >= y2):
    #print(x1,y1,x2,y2)
    out += 1
print(out)

# ------------------------- Part 2 -------------------------#

out=0
for i in data:
  x1,x2,y1,y2 = i[0][0],i[1][0],i[0][1],i[1][1]
  if (x1 <= x2 and y1 >= x2) or (x1 >= x2 and y1 <= y2) or (x1 <= x2 and y1 >= y2) or (x1 <= y2 and y1 >= y2):
    #print(x1,y1,x2,y2)
    out += 1
print(out)


