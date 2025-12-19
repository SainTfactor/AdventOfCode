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
  grid = Grid(data)

  current_loc = grid.find_start()
  cur_tacys = [current_loc]

  ans = 0
  for _ in range(current_loc[1]):
    new_tacys = []
    for t in cur_tacys:
      n,x,y = grid.next(t[0], t[1], grid.Directions.DOWN)
      if n == '^':
        new_tacys.append((x-1, y))
        new_tacys.append((x+1, y))
        ans += 1
      else:
        new_tacys.append((x,y))
        grid.set(x,y,'|')
    cur_tacys = list(set(new_tacys))

  grid.print()
  print(ans)

  # --------------------- Part 2 --------------------- #

  for n,x,y in grid:
    if y == 0 and n == '|':
      grid.set(x,y,1)
      continue

    if n == '|':
      grid.set(x,y,grid.next(x,y,grid.Directions.DOWN)[0])
    if n == '^':
      grid.set(x,y,grid.next(x,y,grid.Directions.DOWN_LEFT)[0] + grid.next(x,y,grid.Directions.DOWN_RIGHT)[0])

  grid.print()

