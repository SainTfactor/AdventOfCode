#!/usr/bin/env python3
import re
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
  target_grid = Grid([["." for j in i] for i in data])

  def mark_up_grid(grid, antennas):
    for i in range(len(antennas)-1):
      for j in range(i+1, len(antennas)):
        point_1 = antennas[i]
        point_2 = antennas[j]
        x_diff = point_1[0] - point_2[0]
        y_diff = point_1[1] - point_2[1]
        point_3 = (point_1[0] + x_diff, point_1[1] + y_diff)
        point_4 = (point_2[0] - x_diff, point_2[1] - y_diff)
        try:
          grid.set(point_3[0], point_3[1], "#")
        except:
          pass
        try:
          grid.set(point_4[0], point_4[1], "#")
        except:
          pass

  valid_antenna = re.compile("[a-zA-Z0-9]")
  antenna_types = [] 
  for node, _, _ in my_grid:
    if valid_antenna.match(node) and not node in antenna_types:
      antenna_types.append(node)

  print(antenna_types)

  for antenna in antenna_types:
    all_of_type = []
    for node, x, y in my_grid:
      if node == antenna:
        all_of_type.append((x,y))
    mark_up_grid(target_grid, all_of_type)

  output = 0
  for node, _, _ in target_grid:
    if node == "#":
      output += 1
  print(output)

  # --------------------- Part 2 --------------------- #

  data = parse_puzzle_input(args.real)
  
  my_grid = Grid(data)
  target_grid = Grid([["." for j in i] for i in data])

  def mark_up_grid(grid, antennas):
    for i in range(len(antennas)-1):
      for j in range(i+1, len(antennas)):
        point_1 = antennas[i]
        point_2 = antennas[j]
        x_diff = point_1[0] - point_2[0]
        y_diff = point_1[1] - point_2[1]
        try:
          point_x = point_1
          while True:
            grid.set(point_x[0], point_x[1], "#")
            point_x = (point_x[0] + x_diff, point_x[1] + y_diff)
        except:
          pass
        try:
          point_x = point_2
          while True:
            grid.set(point_x[0], point_x[1], "#")
            point_x = (point_x[0] - x_diff, point_x[1] - y_diff)
        except:
          pass


  valid_antenna = re.compile("[a-zA-Z0-9]")
  antenna_types = [] 
  for node, _, _ in my_grid:
    if valid_antenna.match(node) and not node in antenna_types:
      antenna_types.append(node)

  print(antenna_types)

  for antenna in antenna_types:
    all_of_type = []
    for node, x, y in my_grid:
      if node == antenna:
        all_of_type.append((x,y))
    mark_up_grid(target_grid, all_of_type)

  my_grid.print()
  print("xxxxxxxxxxxxxxx")
  target_grid.print()
  output = 0
  for node, _, _ in target_grid:
    if node == "#":
      output += 1
  print(output)

