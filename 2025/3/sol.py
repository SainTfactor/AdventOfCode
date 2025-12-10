#!/usr/bin/env python3
import argparse

def parse_puzzle_input(real_data, sample_data_file):
  data_source = "real_data.txt" if real_data else sample_data_file
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  # manipulate data
  def cleaner(line):
    return [int(j) for j in line] # For character map grids

  return [cleaner(i) for i in data]






if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  parser.add_argument("-s", "--sample_file", default="sample_data.txt", help="Specify alternate name for sample data file.  Default: sample_data.txt")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  data = parse_puzzle_input(args.real, args.sample_file)

  res = 0
  for d in data:
    d1i = max(d[0:-1])
    d1 = str(max(d[0:-1]))
    d2 = str(max(d[d.index(d1i)+1:]))
    num = int(d1+d2)
    res += num
  print(res)

  
  # --------------------- Part 2 --------------------- #

  data = parse_puzzle_input(args.real, args.sample_file)

  def get_big_num(lst, size=2):
    ret_arr = []
    my_range = lst[0:1-size]
    remainder = lst[1-size:]
    for i in range(size):
      dig = max(my_range)
      ret_arr.append(str(dig))
      if i < len(remainder):
        my_range += [remainder[i]]
      my_range = my_range[my_range.index(dig)+1:]
    return int("".join(ret_arr))

  res = 0
  for d in data:
    num = get_big_num(d, size=12)
    res += num
  print(res)



