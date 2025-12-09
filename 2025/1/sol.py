#!/usr/bin/env python3
import argparse

def parse_puzzle_input(real_data, sample_data_file):
  data_source = "real_data.txt" if real_data else sample_data_file
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  # manipulate data
  def cleaner(line):
    #return [j for j in line] # For character map grids
    return line

  return [cleaner(i) for i in data]






if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  parser.add_argument("-s", "--sample_file", default="sample_data.txt", help="Specify alternate name for sample data file.  Default: sample_data.txt")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  data = parse_puzzle_input(args.real, args.sample_file)

  start = 50
  ans = 0
  for x in data:
    d = 1 if x[0] == 'R' else -1
    dst = d * int(x[1:])
    start += dst
    while start > 99:
      start -= 100
    while start < 0:
      start += 100
    if start == 0:
      ans += 1
  print(ans)


  # --------------------- Part 2 --------------------- #

  data = parse_puzzle_input(args.real, args.sample_file)


  start = 50
  ans = 0
  for x in data:
    d = 1 if x[0] == 'R' else -1
    dst = d * int(x[1:])
    if start == 0 and d == -1:
      start = 100
    if start == 100 and d == 1:
      start = 0
    start += dst
    while start > 100:
      start -= 100
      ans += 1
    while start < 0:
      start += 100
      ans += 1
    if start in [0,100]:
      ans += 1
  print(ans)

