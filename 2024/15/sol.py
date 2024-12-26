#!/usr/bin/env python3
import argparse
from grid import Grid

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  grid = []
  instructions = []
  
  runner = []
  is_inst = False
  for i in data:
    if i == "":
      grid = runner
      runner = []
      is_inst = True
    if not is_inst:
      runner.append([j for j in i])
    else:
      for j in i:
        runner.append(j)
  instructions = runner

  return Grid(grid), instructions




if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  def get_direction(arrow):
    if arrow == "<":
      return Grid.Directions.LEFT
    elif arrow == ">":
      return Grid.Directions.RIGHT
    elif arrow == "^":
      return Grid.Directions.UP
    elif arrow == "v":
      return Grid.Directions.DOWN
    else:
      raise Exception

  def find_guy(grid):
    for node,x,y in grid:
      if node == "@":
        return x,y
    raise Exception

  def make_move(grid, guy_pos, move, start=True):
    x,y = guy_pos
    direction = get_direction(move)
    next_node, next_x, next_y = grid.next(x,y,direction)
    if next_node == ".":
      if start:
        grid.set(next_x, next_y, "@")
        grid.set(x, y, ".")
      else:
        grid.set(next_x, next_y, "O")
      return True
    if next_node == "#":
      return False
    if next_node == "O":
      ret_val = make_move(grid, (next_x, next_y), move, False)
      if ret_val and start:
        grid.set(next_x,next_y,"@")
        grid.set(x,y,".")
      return ret_val

  def get_box_score(grid, pos):
    max_x, max_y = grid.maxs()
    return ((max_y-pos[1]-1) * 100) + pos[0]

  my_grid, instructions = parse_puzzle_input(args.real)

  for inst in instructions:
    pos = find_guy(my_grid)
    make_move(my_grid, pos, inst)

  my_grid.print()

  total = 0
  for node, x, y in my_grid:
    if node == "O":
      total += get_box_score(my_grid, (x,y))
  print(total)

  # --------------------- Part 2 --------------------- #

  my_grid, instructions = parse_puzzle_input(args.real)



