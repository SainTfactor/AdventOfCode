#!/usr/bin/env python3
from data import data

data = {
  0: {
    "items": [ 79, 98 ],
    "operation": lambda val: val * 19,
    "test": 23,
    "true": 2,
    "false": 3
  },
  1: {
    "items": [ 54, 65, 75, 74 ],
    "operation": lambda val: val + 6,
    "test": 19,
    "true": 2,
    "false": 0
  },
  2: {
    "items": [ 79, 60, 97 ],
    "operation": lambda val: val * val,
    "test": 13,
    "true": 1,
    "false": 3
  },
  3: {
    "items": [ 74 ],
    "operation": lambda val: val + 3,
    "test": 17,
    "true": 0,
    "false": 1
  }
}

print(data)

# --------------------- Part 2 --------------------- #

print(data)
