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

  regions = my_grid.all_regions()

  output = 0
  for region in regions:
    perimeter = 0
    for x,y in region:
      for _, nx, ny in my_grid.neighbors(x,y):
        if my_grid.at(x,y) != my_grid.at(nx,ny):
          perimeter += 1
    #print("{}: {} x {}".format(my_grid.at(region[0][0], region[0][1]), len(region), perimeter))
    output += len(region) * perimeter

  print(output)

  # --------------------- Part 2 --------------------- #

  data = parse_puzzle_input(args.real)
  my_grid = Grid(data)

  regions = my_grid.all_regions()

  def corner_count(grid, x, y):
    node_type = grid.at(x,y)
    direction = Grid.Directions.UP
    count = 0
    for i in range(4):
      av, _, _ = grid.next(x,y,direction)
      bv, _, _ = grid.next(x,y,Grid.Directions.half_turn_right(direction))
      cv, _, _ = grid.next(x,y,Grid.Directions.turn_right(direction))

      corner = "{}{}{}".format(0 if av == node_type else 1, 
                               0 if bv == node_type else 1,
                               0 if cv == node_type else 1)
      if corner == "010" or corner == "111" or corner == "101":
        count += 1

      direction = Grid.Directions.turn_right(direction)
    return count

  output = 0
  for region in regions:
    perimeter = 0
    for x,y in region:
      perimeter += corner_count(my_grid, x, y)
    print("{}: {} x {}".format(my_grid.at(region[0][0], region[0][1]), len(region), perimeter))
    output += len(region) * perimeter

  print(output)


  



