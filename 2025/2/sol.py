#!/usr/bin/env python3
import argparse

def parse_puzzle_input(real_data, sample_data_file):
  data_source = "real_data.txt" if real_data else sample_data_file
  with open(data_source, "r") as f:
    data = f.readlines()[0].strip().split(",")

  # manipulate data
  def cleaner(line):
    stuff = line.split("-")
    return (int(stuff[0]), int(stuff[1]))

  return [cleaner(i) for i in data]



def is_number_bad(num):
  strnum = str(num)
  mylen = len(strnum)
  myhlen = int(mylen/2)
  return mylen % 2 == 0 and strnum[0:myhlen] == strnum[myhlen:]

def is_number_very_bad(num):
  strnum = str(num)
  mylen = len(strnum)
  for i in range(1,int(mylen/2)+1):
    if mylen%i == 0:
      x = strnum[0:i]
      isbad = True
      for j in range(1,int(mylen/i)):
        if strnum[i*j:(i*j)+i] != x:
          isbad = False
          break
      if isbad:
        return True
  return False

if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  parser.add_argument("-s", "--sample_file", default="sample_data.txt", help="Specify alternate name for sample data file.  Default: sample_data.txt")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  data = parse_puzzle_input(args.real, args.sample_file)

  ans = 0
  for i in data:
    for x in range(i[0], i[1]+1):
      if is_number_bad(x):
        ans += x
  print(ans)

  # --------------------- Part 2 --------------------- #

  data = parse_puzzle_input(args.real, args.sample_file)


  ans = 0
  for i in data:
    for x in range(i[0], i[1]+1):
      if is_number_very_bad(x):
        ans += x
  print(ans)

