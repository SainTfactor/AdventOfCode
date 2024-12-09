#!/usr/bin/env python3
import argparse
from grid import Grid


def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [[j for j in i.strip()] for i in f.readlines()]

  # manipulate data

  return data



def make_move(guy, direction, grid):
  node, new_x, new_y =  grid.next(guy[0], guy[1], direction)
  if node != "#":
    grid.set(guy[0],guy[1],"X")
    return (new_x, new_y)
  else:
    return guy


if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  args = parser.parse_args()

  data = parse_puzzle_input(args.real)



  # --------------------- Part 1 --------------------- #
  
  my_grid = Grid(data)

  our_guy = (0,0)
  direction = Grid.Directions.UP

  for node, x, y in my_grid:
    if node == "^":
      our_guy = (x,y)

  try:
    while True:
      new_guy = make_move(our_guy, direction, my_grid)
      if new_guy == our_guy:
        direction = Grid.Directions.turn_right(direction)
      our_guy = new_guy
  except Exception as e:
    #raise e
    #my_grid.print()
    pass
  
  outval = 0
  for node, _, _ in my_grid:
    if node == "X":
      outval += 1
  print(outval)

  # --------------------- Part 2 --------------------- #




