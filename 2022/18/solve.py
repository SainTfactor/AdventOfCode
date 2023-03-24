#!/usr/bin/env python3
from data import data

data = [(2,2,2), (1,2,2), (3,2,2), (2,1,2), (2,3,2), (2,2,1), (2,2,3), (2,2,4), (2,2,6), (1,2,5), (3,2,5), (2,1,5), (2,3,5)]

def check_open_sides(point,grid):
  x,y,z=point
  ret_val = 0
  if not grid[x+1][y][z]:
    ret_val += 1
  if not grid[x-1][y][z]:
    ret_val += 1
  if not grid[x][y+1][z]:
    ret_val += 1
  if not grid[x][y-1][z]:
    ret_val += 1
  if not grid[x][y][z+1]:
    ret_val += 1
  if not grid[x][y][z-1]:
    ret_val += 1
  return ret_val

max_x = max([i[0] for i in data])+2
max_y = max([i[1] for i in data])+2
max_z = max([i[2] for i in data])+2
array_boi = [[[False for z in range(max_z)] for y in range(max_y)] for x in range(max_x)]

for i in data:
  x,y,z = i
  array_boi[x][y][z] = True

total_open_sides = 0
for point in data:
  sides = check_open_sides(point, array_boi)
  total_open_sides += sides

print(total_open_sides)

# --------------------- Part 2 --------------------- #

def clear_neighbors(point,grid):
  pass

gas = [(0,0,0)]
while len(gas) > 0:
  new_gas = []
  for g in gas:
    x,y,z = g
    array_boi[x][y][z] = True
    new_gas += clear_neighbors(g,array_boi)
  gas = list(set(new_gas))

