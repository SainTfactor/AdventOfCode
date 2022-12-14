#!/usr/bin/env python3
from functools import reduce

def reduce_func(runner, val):
  runner.append(val)
  minval = min(runner)
  runner.remove(minval)
  return runner

data = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
from data import data

outs = [sum(i) for i in data]
topthree = reduce(reduce_func, outs, [0,0,0])

print(topthree)
print(sum(topthree))
