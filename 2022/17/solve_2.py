#!/usr/bin/env python3
from data import data

blocks=[]
blocks.append([(0, 0), (1, 0), (2, 0), (3, 0)]) # flat block
blocks.append([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]) # plus block
blocks.append([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]) # backwards L block
blocks.append([(0, 0), (0, 1), (0, 2), (0, 3)]) # vertical block
blocks.append([(0, 0), (0, 1), (1, 0), (1, 1)]) # cube block

data = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

grid = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0)]

def make_rock(rock_type, current_floor, left_justification=2):
  new_rock = []
  for i in rock_type:
    new_rock.append((i[0]+left_justification, i[1] + current_floor + 4))
  return new_rock

def print_grid(grid):
  start_height=max([i[1] for i in grid]) + 5
  for y in range(start_height, 0, -1):
    for x in range(7):
      print('#' if (x,y) in grid else '.', end="")
    print()

def move_and_check(grid, rock, xdir, ydir):
  collision=False
  new_rock =[]
  for node in range(len(current_rock)):
    new_rock.append((current_rock[node][0]+xdir, current_rock[node][1]+ydir))

  for node in new_rock:
    if node in grid:
      collision = True

  ret_rock = rock if collision else new_rock
  return ret_rock, collision

beat_height = 0
rocks_in_beat = 0
orpb = 0

rocks_fallen = 0
rocks_mod = 5
cycle_current = 0
cycle_mod = len(data)

print("cycle - height - change - x_more_rocks")
while rocks_fallen < 1000000000000:
  rocks_in_beat += 1
  #print(rocks_fallen%rocks_mod, cycle_current%cycle_mod)
  if cycle_current%cycle_mod == 5 and rocks_fallen%rocks_mod == 0:
    obh = beat_height
    beat_height = max([i[1] for i in grid])
    print("{} - {} - {} - {}".format(cycle_current, beat_height, beat_height - obh, rocks_in_beat-orpb))
    orpb = rocks_in_beat
  current_height = max([i[1] for i in grid])
  current_rock = make_rock(blocks[rocks_fallen%rocks_mod], current_height)
  rock_landed=False
  while not rock_landed:  
    direction = data[cycle_current % cycle_mod]

    if direction == '<':
      left_edge=min([i[0] for i in current_rock])
      if left_edge > 0:
        current_rock, _ = move_and_check(grid, current_rock, -1, 0)
    else:
      right_edge=max([i[0] for i in current_rock])
      if right_edge < 6:
        current_rock, _ = move_and_check(grid, current_rock, 1, 0)
    
    current_rock, rock_landed = move_and_check(grid, current_rock, 0, -1)
    if rock_landed:
      for node in current_rock:
        grid.append(node)

    cycle_current += 1
  rocks_fallen+=1

#print_grid(grid)
print(max([i[1] for i in grid]))
# --------------------- Part 2 --------------------- #

