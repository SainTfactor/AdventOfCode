#!/usr/bin/env python3
import argparse
from grid import Grid

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  # manipulate data
  def cleaner(line):
    return [int(j) for j in line] # For character map grids

  return [cleaner(i) for i in data]






if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  args = parser.parse_args()


  # --------------------- Part 1 --------------------- #

  data = parse_puzzle_input(args.real)

  my_grid = Grid(data)

  def get_head_score(space, grid):
    tops = []
    current_loc = grid.at(space[0],space[1])
    direction = Grid.Directions.UP
    if current_loc == 8:
      for i in range(4):
        node, x, y = grid.next(space[0], space[1], direction)
        if node == 9:
          tops.append((x,y))
        direction = Grid.Directions.turn_right(direction)
    else:
      for i in range(4):
        node, x, y = grid.next(space[0], space[1], direction)
        if node == (current_loc + 1):
          tops += get_head_score((x,y), grid)
        direction = Grid.Directions.turn_right(direction)
    return tops
  
  heads = []
  for node, x, y in my_grid:
    if node == 0:
      heads.append((x,y))

  happy_head_score = 0
  for head in heads:
    score = get_head_score(head, my_grid)
    uniq = set(score)
    print(head, uniq)
    happy_head_score += len(uniq)

  print(happy_head_score)

  # --------------------- Part 2 --------------------- #
  
  def get_head_score(space, grid):
    tops = 0
    current_loc = grid.at(space[0],space[1])
    direction = Grid.Directions.UP
    if current_loc == 8:
      for i in range(4):
        node, x, y = grid.next(space[0], space[1], direction)
        if node == 9:
          tops += 1
        direction = Grid.Directions.turn_right(direction)
    else:
      for i in range(4):
        node, x, y = grid.next(space[0], space[1], direction)
        if node == (current_loc + 1):
          tops += get_head_score((x,y), grid)
        direction = Grid.Directions.turn_right(direction)
    return tops

  data = parse_puzzle_input(args.real)
  
  heads = []
  for node, x, y in my_grid:
    if node == 0:
      heads.append((x,y))

  happy_head_score = 0
  for head in heads:
    score = get_head_score(head, my_grid)
    print(head, score)
    happy_head_score += score

  print(happy_head_score)

  my_grid = Grid(data)


