#!/usr/bin/env python3
import argparse
import traceback
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
  
  def do_thing(my_grid, max_run=200000):
    our_guy = (0,0)
    direction = Grid.Directions.UP
  
    for node, x, y in my_grid:
      if node == "^":
        our_guy = (x,y)
  
    for i in range(max_run):
      new_guy = make_move(our_guy, direction, my_grid)
      if new_guy == our_guy:
        direction = Grid.Directions.turn_right(direction)
      our_guy = new_guy

  try:
    do_thing(my_grid)
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

  print(len(data) * len(data[0]))
   
  prog = 0
  good_count = 0
  data = parse_puzzle_input(args.real)
  my_grid = Grid(data)
  for node, x, y in my_grid:
    prog += 1
    if prog % 10 == 0:
      print(prog)
    data = parse_puzzle_input(args.real)
    temp_grid = Grid(data)
    temp_grid.set(x,y,"#")
    ends=False
    try:
      do_thing(temp_grid)
    except Exception as e:
      ends=True
    if not ends:
      good_count += 1
  print(good_count)
      

