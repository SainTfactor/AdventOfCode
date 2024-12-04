#!/usr/bin/env python3
import argparse

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  return data


# 0,0 is bottom left, so translation is needed
def grid_at(x,y,grid):
  if y == len(grid):
    return None #out of bounds
  if x == len(grid[0]):
    return None #out of bounds
  if x < 0 or y < 0:
    return None #out of bounds
  return grid[len(grid)-y-1][x]

def print_grid(grid):
  for i in grid:
    print("".join(i))

def grid_maxs(grid):
  #returns max_x and max_y
  return len(grid[0]), len(grid)

def generate_grid_scan(grid):
  max_x, max_y = grid_maxs(grid)
  for y in range(max_y):
    for x in range(max_x):
      yield x,y

def get_next(x, y, grid, direction):
  if direction == 0:
    return grid_at(x,y+1,grid), x, y+1
  elif direction == 1:
    return grid_at(x+1,y+1,grid), x+1, y+1
  elif direction == 2:
    return grid_at(x+1,y,grid), x+1, y
  elif direction == 3:
    return grid_at(x+1,y-1,grid), x+1, y-1
  elif direction == 4:
    return grid_at(x,y-1,grid), x, y-1
  elif direction == 5:
    return grid_at(x-1,y-1,grid), x-1, y-1
  elif direction == 6:
    return grid_at(x-1,y,grid), x-1, y
  elif direction == 7:
    return grid_at(x-1,y+1,grid), x-1, y+1
  else:
    raise Exception

def if_x_word_count(x,y,grid):
  if grid_at(x,y,grid) != "X":
    return 0
  
  count = 0
  for i in range(8):
    next_letter, new_x, new_y = get_next(x, y, grid, i)
    if next_letter != "M":
      continue
    next_letter, new_x, new_y = get_next(new_x, new_y, grid, i)
    if next_letter != "A":
      continue
    next_letter, new_x, new_y = get_next(new_x, new_y, grid, i)
    if next_letter != "S":
      continue
    count += 1

  return count

def if_a_word_count(x,y,grid):
  if grid_at(x,y,grid) != "A":
    return 0
  
  top_left,_,_ = get_next(x,y,grid,7)
  top_right,_,_ = get_next(x,y,grid,1)
  bottom_left,_,_ = get_next(x,y,grid,5)
  bottom_right,_,_ = get_next(x,y,grid,3)

  backslash = False
  forwardslash = False
  if (top_left == "M" and bottom_right == "S") or (top_left == "S" and bottom_right == "M"):
    backslash = True
  if (top_right == "M" and bottom_left == "S") or (top_right == "S" and bottom_left == "M"):
    forwardslash = True

  return backslash and forwardslash

if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  args = parser.parse_args()

  data = parse_puzzle_input(args.real)

  # --------------------- Part 1 --------------------- #

  word_count = 0
  for x,y in generate_grid_scan(data):
    word_count += if_x_word_count(x,y,data)
  print(word_count)

  # --------------------- Part 2 --------------------- #

  word_count = 0
  for x,y in generate_grid_scan(data):
    word_count += 1 if if_a_word_count(x,y,data) else 0
  print(word_count)



