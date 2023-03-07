#!/usr/bin/env python3
from data import data

blocks=[]
blocks.append([(0, 0), (0, 1), (0, 2), (0, 3)]) # flat block
blocks.append([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]) # plus block
blocks.append([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]) # backwards L block
blocks.append([(0, 0), (0, 1), (1, 0), (1, 1)]) # cube block
blocks.append([(0, 1), (1, 0), (2, 0), (3, 0)]) # vertical block

data = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

def make_rock(rock_type, current_floor, left_justification=2):
  new_rock = []
  for i in rock_type:
    new_rock.append((i[0]+left_justification, i[1] + current_floor + 3))
  return new_rock

current_height = 0
rocks_fallen = 0
rocks_mod = 5
cycle_current = 0
cycle_mod = len(data)
current_rock = make_rock(blocks[rocks_fallen]%rocks_mod, current_height)

while rocks_fallen < 2022:
  direction = data[cycle_current % cycle_mod]

  #stuff

  cycle_current += 1

# --------------------- Part 2 --------------------- #

