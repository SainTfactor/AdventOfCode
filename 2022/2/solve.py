#!/usr/bin/env python3
from data import data

#data = [("A", "Y"), ("B", "X"), ("C", "Z")]


outcomes = {
    "A" : {
      "X" : 3,
      "Y" : 6,
      "Z" : 0
    },
    "B" : {
      "X" : 0,
      "Y" : 3,
      "Z" : 6
    },
    "C" : {
      "X" : 6,
      "Y" : 0,
      "Z" : 3
    },
  }

my_throw_values = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
  }

score = 0
for i in data:
  #print(my_throw_values[i[1]], outcomes[i[0]][i[1]])
  score += my_throw_values[i[1]] + outcomes[i[0]][i[1]]
print(score)

# --------------------- Part 2 --------------------- #

outcomes = {
    "X" : {
      "A" : 3, 
      "B" : 1, 
      "C" : 2 
    },
    "Y" : {
      "A" : 3+1, 
      "B" : 3+2, 
      "C" : 3+3 
    },
    "Z" : {
      "A" : 6+2, 
      "B" : 6+3, 
      "C" : 6+1 
    }
  }

score = 0
for i in data:
  #print(outcomes[i[1]][i[0]])
  score += outcomes[i[1]][i[0]]
print(score)

