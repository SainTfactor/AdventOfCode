#!/usr/bin/env python3
import argparse
from grid import Grid

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  return data


def if_x_word_count(x,y,grid):
  if grid.at(x,y) != "X":
    return 0
  
  count = 0
  for direction in Grid.Directions.get_all():
    next_letter, new_x, new_y = grid.next(x, y, direction)
    if next_letter != "M":
      continue
    next_letter, new_x, new_y = grid.next(new_x, new_y, direction)
    if next_letter != "A":
      continue
    next_letter, new_x, new_y = grid.next(new_x, new_y, direction)
    if next_letter != "S":
      continue
    count += 1

  return count

def if_a_word_count(x,y,grid):
  if grid.at(x,y) != "A":
    return 0
  
  top_left,_,_ = grid.next(x,y,Grid.Directions.UP_LEFT)
  top_right,_,_ = grid.next(x,y,Grid.Directions.UP_RIGHT)
  bottom_left,_,_ = grid.next(x,y,Grid.Directions.DOWN_LEFT)
  bottom_right,_,_ = grid.next(x,y,Grid.Directions.DOWN_RIGHT)

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
  my_grid = Grid(data)

  # --------------------- Part 1 --------------------- #

  word_count = 0
  for x,y in my_grid.generate_grid_scan():
    word_count += if_x_word_count(x,y,my_grid)
  print(word_count)

  # --------------------- Part 2 --------------------- #

  word_count = 0
  for x,y in my_grid.generate_grid_scan():
    word_count += 1 if if_a_word_count(x,y,my_grid) else 0
  print(word_count)



