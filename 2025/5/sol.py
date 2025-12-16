#!/usr/bin/env python3
import argparse

def parse_puzzle_input(real_data, sample_data_file):
  data_source = "real_data.txt" if real_data else sample_data_file
  with open(data_source, "r") as f:
    data_in = f.read()
    ranges = [i.strip() for i in data_in.split("\n\n")[0].split("\n") if i != ""]
    items = [i.strip() for i in data_in.split("\n\n")[1].split("\n") if i != ""]

  # manipulate data
  def cleaner(line):
    #return [j for j in line] # For character map grids
    items = line.split("-")
    return [int(items[0]), int(items[1])]

  return [cleaner(i) for i in ranges], [int(i) for i in items]




def check_in_range(num, myrange):
  return num <= myrange[1] and num >= myrange[0]


if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  parser.add_argument("-s", "--sample_file", default="sample_data.txt", help="Specify alternate name for sample data file.  Default: sample_data.txt")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  ranges, items = parse_puzzle_input(args.real, args.sample_file)

  ans = 0
  for i in items:
    for r in ranges:
      if check_in_range(i, r):
        ans += 1
        break
  print(ans)


  # --------------------- Part 2 --------------------- #

  ranges, items = parse_puzzle_input(args.real, args.sample_file)

  ranges = sorted(ranges, key = lambda x: x[0])

  done = False
  while not done:
    done = True
    for ri in range(len(ranges) - 1):
      cur_range = ranges[ri]
      nxt_range = ranges[ri+1]
      if cur_range[1] >= nxt_range[0]:
        if cur_range[1] >= nxt_range[1]:
          nxt_range[0] = cur_range[0]
          nxt_range[1] = cur_range[1]
        else:
          cur_range[1] = nxt_range[1]
          nxt_range[0] = cur_range[0]
    len_r = len(ranges)
    ranges = list({"-".join(str(j)) : j for j in ranges}.values())
    if len_r > len(ranges):
      done = False

  ans = 0
  for r in ranges:
    ans += r[1] - r[0] + 1

  print(ans)

