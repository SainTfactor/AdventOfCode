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

def parse_puzzle_input_2(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  grid = []
  instructions = []
  
  def line_buffer(line):
    ret_val = []
    for i in line:
      if i == ".":
        ret_val += [".", "."]
      if i == "O":
        ret_val += ["[", "]"]
      if i == "#":
        ret_val += ["#", "#"]
      if i == "@":
        ret_val += ["@", "."]
    return ret_val

  runner = []
  is_inst = False
  for i in data:
    if i == "":
      grid = runner
      runner = []
      is_inst = True
    if not is_inst:
      runner.append(line_buffer(i))
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

  def check_move_vert(grid, guy_pos, move, prev_node="@"):
    x,y = guy_pos
    direction = get_direction(move)
    straight_next_node, straight_next_x, straight_next_y = grid.next(x,y,direction)
    if straight_next_node == "]":
      left_next_node, left_next_x, left_next_y = grid.next(straight_next_x, straight_next_y, Grid.Directions.LEFT)
      return check_move_vert(grid, (straight_next_x, straight_next_y), move, straight_next_node) and check_move_vert(grid, (left_next_x, left_next_y), move, left_next_node)
    elif straight_next_node == "[":
      right_next_node, right_next_x, right_next_y = grid.next(straight_next_x, straight_next_y, Grid.Directions.RIGHT)
      return check_move_vert(grid, (straight_next_x, straight_next_y), move, straight_next_node) and check_move_vert(grid, (right_next_x, right_next_y), move, right_next_node)
    elif straight_next_node == ".":
      return True
    elif straight_next_node == "#":
      return False
    else:
      raise Exception
    

  def make_move_vert(grid, guy_pos, move, prev_node="@"):
    x,y = guy_pos
    direction = get_direction(move)
    straight_next_node, straight_next_x, straight_next_y = grid.next(x,y,direction)
    if straight_next_node == "]":
      left_next_node, left_next_x, left_next_y = grid.next(straight_next_x, straight_next_y, Grid.Directions.LEFT)
      make_move_vert(grid, (left_next_x, left_next_y), move, left_next_node)
      make_move_vert(grid, (straight_next_x, straight_next_y), move, straight_next_node)
    elif straight_next_node == "[":
      right_next_node, right_next_x, right_next_y = grid.next(straight_next_x, straight_next_y, Grid.Directions.RIGHT)
      make_move_vert(grid, (right_next_x, right_next_y), move, right_next_node)
      make_move_vert(grid, (straight_next_x, straight_next_y), move, straight_next_node)

    grid.set(straight_next_x, straight_next_y, prev_node)
    grid.set(x,y,".")
    

  def make_move_hori(grid, guy_pos, move, prev_node="@"):
    x,y = guy_pos
    direction = get_direction(move)
    nnode, nx, ny = grid.next(x,y,direction)
    worked = False
    if nnode == "#":
      return False
    elif nnode == ".":
      grid.set(nx,ny,prev_node)
      return True
    else:
      worked = make_move_hori(grid, (nx,ny), move, nnode)

    if worked:
      grid.set(nx,ny,prev_node)
    return worked

  def make_move(grid, guy_pos, move):
    direction = get_direction(move)
    worked = False
    if direction == Grid.Directions.UP or direction == Grid.Directions.DOWN:
      if check_move_vert(grid, guy_pos, move):
        make_move_vert(grid, guy_pos, move)
        worked = True
    else:
      worked = make_move_hori(grid, guy_pos, move)

    if worked:
      x,y = guy_pos
      grid.set(x,y,".")



  my_grid, instructions = parse_puzzle_input_2(args.real)

  for inst in instructions:
    pos = find_guy(my_grid)
    make_move(my_grid, pos, inst)

  my_grid.print()
  
  total = 0
  for node, x, y in my_grid:
    if node == "[":
      total += get_box_score(my_grid, (x,y))
  print(total)

