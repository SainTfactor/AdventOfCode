#!/usr/bin/env python3
import argparse
from grid import Grid

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  def objectify(item):
    return { "tile" : item, "cost" : -1, "updated_count" : 0, "previous_node" : None }

  # manipulate data
  def cleaner(line):
    return [objectify(j) for j in line] # For character map grids

  return [cleaner(i) for i in data]


if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  def get_start_and_end(grid):
    start = None
    end = None
    for node, x, y in grid:
      if node["tile"] == "S":
        start = (x,y)
      elif node["tile"] == "E":
        end = (x,y)
    return start, end

  # Had to reimplement iteratively, because you hit the recusion limit otherwise
  def walk_maze(grid, entry, ceiling=100000):
    stack = [{ "start" : entry, "current_total" : 0, "current_direction" : Grid.Directions.RIGHT, "previous" : entry}]
    while len(stack) > 0:
      item = stack.pop()
      start = item["start"]
      current_total = item["current_total"]
      current_direction = item["current_direction"]
      previous = item["previous"]

      current_node = grid.at(*start)
      if current_node["tile"] == "#":
        continue # hit wall
      if current_node["cost"] <= current_total and current_node["cost"] != -1:
        continue # exit if bad path
      if current_total > ceiling:
        continue # nothing gets this big in reality

      current_node["cost"] = current_total
      current_node["updated_count"] += 1
      current_node["previous_node"] = previous

      if start ==  (129,118):
        print(118, item, current_node)

      direction = current_direction

      for turncost in [1001,2001,1001,1]: # left, back, right, straight
        direction = Grid.Directions.turn_left(direction)
        next_node, next_x, next_y = grid.next(*start, direction)
        stack.append({ "start" : (next_x, next_y), "current_total" : current_total + turncost, "current_direction" : direction, "previous" : start})
      


  data = parse_puzzle_input(args.real)
  my_grid = Grid(data)
  my_grid.print(lambda x: x["tile"])
  
  start, end = get_start_and_end(my_grid)
  print(start,end)
  walk_maze(my_grid, start)


  current_loc = my_grid.at(*end)["previous_node"]
  while my_grid.at(*current_loc)["tile"] != "S":
    my_grid.at(*current_loc)["tile"] = "O"
    current_loc = my_grid.at(*current_loc)["previous_node"]

  my_grid.print(lambda x: x["tile"])

  for n,x,y in my_grid:
    if n["tile"] == "E":
      print("({},{}) : {}".format(x,y,n))
  print(end)

  # --------------------- Part 2 --------------------- #

  print("PART 2!!!!!")

  def get_start_and_end(grid):
    start = None
    end = None
    for node, x, y in grid:
      if node == "S":
        start = (x,y)
      elif node == "E":
        end = (x,y)
    return start, end
  
  def parse_puzzle_input(real_data=False):
    data_source = "real_data.txt" if real_data else "sample_data.txt"
    with open(data_source, "r") as f:
      data = [i.strip() for i in f.readlines()]
 
    # manipulate data
    def cleaner(line):
      return [j for j in line] # For character map grids

    return [cleaner(i) for i in data]

  data = parse_puzzle_input(args.real)
  my_grid = Grid(data)

  start, end = get_start_and_end(my_grid)
  
  def cost_function(grid, n, x, y):
    n["visited"] = True
    if not "direction" in n:
      n["direction"] = Grid.Directions.RIGHT
    direction = n["direction"]
    for turncost in [1001,2001,1001,1]: # left, back, right, straight
      direction = Grid.Directions.turn_left(direction)
      next_node, next_x, next_y = grid.next(x, y, direction)
      if next_node["tile"] != "#":
        if next_node["distance"] == None or next_node["distance"] > (turncost + n["distance"]):
          next_node["distance"] = turncost + n["distance"]
          next_node["direction"] = direction
          next_node["previous_node"] = (x,y)

  my_grid.calculate_path_costs(start, cost_function=cost_function)

  final = my_grid.path_cost_to(end)
  print(final)

  def val_np(cur, nxt):
    return cur - 1 ==  nxt or cur - 1001 == nxt or cur + 999 == nxt
  my_grid.print_paths(end,valid_next_step_function=val_np)

  def total_cost(grid):
    ret_val = 0
    for n,x,y in grid:
      if "path_part" in n:
        ret_val += 1
    return ret_val
  total = my_grid.calculate_cost_total(total_cost)
  print(total)
