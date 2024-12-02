#!/usr/bin/env python3
from cols import *

slc = sorted(left_col)
src = sorted(right_col)

summative = 0
for i in range(len(slc)):
  summative += abs(slc[i] - src[i])
print(summative)

#part 2

prody = 0
for i in slc: 
  cnt = len([j for j in src if j == i])
  prody += i*cnt

print(prody)
