#!/usr/bin/env python3
import re
import math
import argparse

def parse_puzzle_input(real_data, sample_data_file):
  data_source = "real_data.txt" if real_data else sample_data_file
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  # manipulate data
  def cleaner(line):
    return [j for j in re.sub('\s+', " ",  line).split(" ")] # For character map grids

  return [cleaner(i) for i in data]






if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  parser.add_argument("-s", "--sample_file", default="sample_data.txt", help="Specify alternate name for sample data file.  Default: sample_data.txt")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  data = parse_puzzle_input(args.real, args.sample_file)

  ans = 0
  for col_num in range(len(data[0])):
    col_items = [int(i[col_num]) for i in data[0:-1]]
    act = data[-1][col_num]
    if act == "+":
      ans += sum(col_items)
    else:
      ans += math.prod(col_items)

  print(ans)

  # --------------------- Part 2 --------------------- #

  def parse_puzzle_input(real_data, sample_data_file):
    data_source = "real_data.txt" if real_data else sample_data_file
    with open(data_source, "r") as f:
      data = [list(i) for i in f.readlines()]
      data = [[j for j in i if j != '\n'] for i in data]
  
    for i in range(len(data[0])):
      blanc_col = True
      for d in data:
        if d[i] != " ":
          blanc_col = False
          break
      if blanc_col:
        for d in data:
          d[i] = "~"
    
    # manipulate data
    def cleaner(line):
      return [j for j in "".join(line).split("~")] # For character map grids
  
    return [cleaner(i) for i in data]


  data = parse_puzzle_input(args.real, args.sample_file)

  ans = 0
  for col_num in range(len(data[0])):
    col_items = [i[col_num] for i in data[0:-1]]
    act = data[-1][col_num].strip()

    nums = [""]*len(col_items[0])
    for i in range(len(col_items)):
      for j in range(len(nums)):
        nums[j] += col_items[i][j]
    col_items = [int(i) for i in nums]

    if act == "+":
      ans += sum(col_items)
    else:
      ans += math.prod(col_items)

  print(ans)

