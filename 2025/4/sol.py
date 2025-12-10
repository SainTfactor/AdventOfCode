#!/usr/bin/env python3
import argparse
from grid import Grid


def parse_puzzle_input(real_data, sample_data_file):
  data_source = "real_data.txt" if real_data else sample_data_file
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  # manipulate data
  def cleaner(line):
    return [j for j in line] # For character map grids

  return [cleaner(i) for i in data]






if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  parser.add_argument("-s", "--sample_file", default="sample_data.txt", help="Specify alternate name for sample data file.  Default: sample_data.txt")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  data = parse_puzzle_input(args.real, args.sample_file)
  my_grid = Grid(data)

  #my_grid.print()
  #print()

  ans = 0
  for node, x, y in my_grid:
    if node == "@":
      count = 0
      for nnode, nx, ny in my_grid.all_neighbors(x,y):
        if nnode in ["@", "X"]:
          count += 1
      if count < 4:
        my_grid.set(x,y,"X")
        ans += 1

  #my_grid.print()
  print(ans)

  # --------------------- Part 2 --------------------- #

  data = parse_puzzle_input(args.real, args.sample_file)

  my_grid = Grid(data)

  my_grid.print()
  print()

  ans = 1
  remd = 0
  while ans > 0:
    ans = 0
    for node, x, y in my_grid:
      if node == "@":
        count = 0
        for nnode, nx, ny in my_grid.all_neighbors(x,y):
          if nnode in ["@"]:
            count += 1
        if count < 4:
          my_grid.set(x,y,".")
          ans += 1
          remd += 1

  my_grid.print()
  print(remd)


