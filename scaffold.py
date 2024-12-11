#!/usr/bin/env python3
import argparse

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
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
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  data = parse_puzzle_input(args.real)



  # --------------------- Part 2 --------------------- #

  data = parse_puzzle_input(args.real)



