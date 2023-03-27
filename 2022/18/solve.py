#!/usr/bin/env python3

from data import data

#data = [(2,2,2), (1,2,2), (3,2,2), (2,1,2), (2,3,2), (2,2,1), (2,2,3), (2,2,4), (2,2,6), (1,2,5), (3,2,5), (2,1,5), (2,3,5)]

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
  x,y,z=point
  ret_val = []
  if (x+1) < len(grid) and not grid[x+1][y][z]:
    ret_val.append((x+1,y,z))
  if (x-1) >= 0 and not grid[x-1][y][z]:
    ret_val.append((x-1,y,z))
  if (y+1) < len(grid[x]) and not grid[x][y+1][z]:
    ret_val.append((x,y+1,z))
  if (y-1) >= 0 and not grid[x][y-1][z]:
    ret_val.append((x,y-1,z))
  if (z+1) < len(grid[x][y]) and not grid[x][y][z+1]:
    ret_val.append((x,y,z+1))
  if (z-1) >= 0 and not grid[x][y][z-1]:
    ret_val.append((x,y,z-1))
  return ret_val

gas = [(0,0,0)]
while len(gas) > 0:
  new_gas = []
  for g in gas:
    x,y,z = g
    array_boi[x][y][z] = True
    new_gas += clear_neighbors(g,array_boi)
  gas = list(set(new_gas))


data2 = []
for x in range(len(array_boi)):
  for y in range(len(array_boi[x])):
    for z in range(len(array_boi[x][y])):
      array_boi[x][y][z] = not array_boi[x][y][z]
      if array_boi[x][y][z]:
        data2.append((x,y,z))


new_total_open_sides = 0
for point in data2:
  sides = check_open_sides(point, array_boi)
  new_total_open_sides += sides

print(new_total_open_sides)
print("Final: {}".format(total_open_sides - new_total_open_sides))
