#!/usr/bin/env python3
from data import data
import functools

data = [([1,1,3,1,1], [1,1,5,1,1]), ([[1],[2,3,4]], [[1],4]), ([9], [[8,7,6]]), ([[4,4],4,4], [[4,4],4,4,4]), ([7,7,7,7], [7,7,7]), ([], [3]), ([[[]]], [[]]), ([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9])]

def compare(x,y):
  if type(x) == int and type(y) == int:
    if x > y:
      return -1
    elif x < y:
      return 1
    else:
      return 0
  elif type(x) == list and type(y) == int:
    return compare(x, [y])
  elif type(x) == int and type(y) == list:
    return compare([x], y)
  elif type(x) == list and type(y) == list:
    retval = 0
    for i in range(min([len(x), len(y)])):
      retval = compare(x[i], y[i])
      if retval != 0:
        return retval
    if retval == 0:
      if len(x) < len(y):
        return 1
      elif len(x) > len(y):
        return -1
      else:
        return 0

truthies = []
for i in range(len(data)):
  item = data[i]
  test_val = compare(item[0], item[1])
  if test_val == 1:
    truthies.append(i+1)

print(truthies)
print(sum(truthies))
  

# --------------------- Part 2 --------------------- #

from data2 import data2
#data2 = [[1,1,3,1,1], [1,1,5,1,1], [[1],[2,3,4]], [[1],4], [9], [[8,7,6]], [[4,4],4,4], [[4,4],4,4,4], [7,7,7,7], [7,7,7], [], [3], [[[]]], [[]], [1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]]

data2.append([[2]])
data2.append([[6]])

print('-'*100)
output = sorted(data2, key=functools.cmp_to_key(compare), reverse=True)
[print(i) for i in output]

print('-'*100)
v1 = output.index([[2]]) + 1
v2 = output.index([[6]]) + 1
print(v1, v2, v1*v2)
