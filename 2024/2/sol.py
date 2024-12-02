#!/usr/bin/env python3

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = f.readlines()

  # manipulate data

  return data

data = parse_puzzle_input()
#data = parse_puzzle_input(True)



# --------------------- Part 2 --------------------- #


