#!/usr/bin/env python3
from data import data

#data = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]

scores = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum_value = 0
for i in data:
  one = i[0:int(len(i)/2)]
  two = i[int(len(i)/2):]
  for j in one:
    try:
      two.index(j)
      sum_value += scores.index(j)
      #print(scores.index(j))
      break
    except:
      continue

print(sum_value)

# --------------------- Part 2 --------------------- #

sum_value = 0
for i in range(0,len(data),3):
  vals = data[i:i+3]
  #print(vals)
  for v in vals[0]:
    try:
      vals[1].index(v)
      vals[2].index(v)
      #print(v)
      sum_value += scores.index(v)
      break
    except:
      continue

print(sum_value)
