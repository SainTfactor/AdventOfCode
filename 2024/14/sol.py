#!/usr/bin/env python3
import re
import argparse
from grid import Grid

def reset_grid(real_data = False):
  if not real_data:
    x_width, y_width = 11,7
  else:
    x_width, y_width = 101,103
  
  mappy = []
  for y in range(y_width):
    mappy.append([{ "robots" : [] } for _ in range(x_width)])

  return Grid(mappy)

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]
  
  if not real_data:
    x_width, y_width = 11,7
  else:
    x_width, y_width = 101,103
  

  all_robots = []

  numchk = re.compile("p=(\d+),(\d+) v=([\-\d]+),([\-\d]+)")
  for item in data:
    groups = [int(i) for i in numchk.search(item).groups()]
    position = (groups[0], y_width - groups[1] - 1)
    velocity = (groups[2], 0-groups[3])

    all_robots.append({ "position" : position,  "velocity" : velocity })

  return all_robots






if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  my_grid = reset_grid(args.real)
  all_robots = parse_puzzle_input(args.real)

  max_x, max_y = my_grid.maxs()
  num_iter = 100
  for robot in all_robots:
    final_x = (robot["position"][0] + (robot["velocity"][0]*num_iter)) % max_x
    final_y = (robot["position"][1] + (robot["velocity"][1]*num_iter)) % max_y
    node = my_grid.at(final_x, final_y)
    node["robots"].append(node)

  my_grid.print(lambda x: str(len(x["robots"])))

  cutoff_x = int(max_x/2)
  cutoff_y = int(max_y/2)
  q1, q2, q3, q4 = 0, 0, 0, 0
  for node,x,y in my_grid:
    if x < cutoff_x and y > cutoff_y:
      q1 += len(node["robots"])
    elif x > cutoff_x and y > cutoff_y:
      q2 += len(node["robots"])
    elif x < cutoff_x and y < cutoff_y:
      q3 += len(node["robots"])
    elif x > cutoff_x and y < cutoff_y:
      q4 += len(node["robots"])

  print(q1,q2,q3,q4)
  print(q1*q2*q3*q4)
  
  # --------------------- Part 2 --------------------- #

  my_grid = reset_grid(args.real)
  all_robots = parse_puzzle_input(args.real)

  print("Doesn't work with sample data.  First result should be the tree for the real data")
  print("This shows you when 10 things are horizontally aligned, so you can spot check if there's a tree.")

  max_x, max_y = my_grid.maxs()
  num_iter = 0
  while True:
    for robot in all_robots:
      final_x = (robot["position"][0] + (robot["velocity"][0]*num_iter)) % max_x
      final_y = (robot["position"][1] + (robot["velocity"][1]*num_iter)) % max_y
      node = my_grid.at(final_x, final_y)
      node["robots"].append(node)

    seq = 0
    good = False
    for i,_,_ in my_grid:
      if len(i["robots"]) > 0:
        seq += 1
      else:
        seq = 0
      if seq > 10:
        good = True
        break

    if good:
      my_grid.print(lambda x: "#" if len(x["robots"]) > 0 else " ")
      print("^ At {}".format(num_iter))
      input("Press enter for next...")
    my_grid = reset_grid(args.real)
    num_iter += 1
    if num_iter % 100 == 0:
      print(num_iter)

