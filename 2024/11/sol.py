#!/usr/bin/env python3
import argparse

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  # manipulate data
  def cleaner(line):
    return [int(i) for i in line.split(" ")]

  return cleaner(data[0])






if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  args = parser.parse_args()

  cache = {}

  # --------------------- Part 1 --------------------- #

  data = parse_puzzle_input(args.real)

  def get_size(num, iterations=25):
    global cache
    
    key = "{}-{}".format(num, iterations)
    if key in cache:
      return cache[key]

    if iterations == 1:
      if len(str(num)) % 2 != 0:
        return 1
      else:
        return 2
    
    if len(str(num)) % 2 == 0:
      strnum = str(num)
      num1 = int(strnum[0:int(len(strnum)/2)])
      num2 = int(strnum[int(len(strnum)/2):])
      retval =  get_size(num1, iterations - 1) + get_size(num2, iterations - 1)
      cache[key] = retval
      return retval

    if num == 0:
      retval =  get_size(1, iterations - 1)
      cache[key] = retval
      return retval

    retval =  get_size(num * 2024, iterations - 1)
    cache[key] = retval
    return retval

  outval = 0
  for i in data:
    outval += get_size(i)
  print(outval)

  # --------------------- Part 2 --------------------- #

  data = parse_puzzle_input(args.real)

  outval = 0
  for i in data:
    outval += get_size(i, 75)
  print(outval)


