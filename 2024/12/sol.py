#!/usr/bin/env python3
import argparse
from grid import Grid

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  # manipulate data
  def cleaner(line):
    return [j for j in line] # For character map grids

  return [cleaner(i) for i in data]






if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  data = parse_puzzle_input(args.real)
  my_grid = Grid(data)

  regions = []
  all_matched_nodes = []
  for node, x, y in my_grid:
    if not (x,y) in all_matched_nodes:
      region = my_grid.region(x,y)
      regions.append(region)
      for item in region:
        all_matched_nodes.append(item)
  
  output = 0
  for region in regions:
    perimeter = 0
    for x,y in region:
      for _, nx, ny in my_grid.neighbors(x,y):
        if my_grid.at(x,y) != my_grid.at(nx,ny):
          perimeter += 1
    print("{}: {} x {}".format(my_grid.at(region[0][0], region[0][1]), len(region), perimeter))
    output += len(region) * perimeter

  print(output)

  # --------------------- Part 2 --------------------- #

  data = parse_puzzle_input(args.real)
  my_grid = Grid(data)




