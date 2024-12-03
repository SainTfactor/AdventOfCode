#!/usr/bin/env python3
import re

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = f.read()

  return data

data = parse_puzzle_input()
#data = parse_puzzle_input(True)

all_muls = re.compile('mul\(\d+,\d+\)', re.MULTILINE)
num_pairs = re.compile('\d+,\d+') 

output=0
for pair in all_muls.findall(data):
  nums = num_pairs.findall(pair)[0].split(",")
  output += int(nums[0]) * int(nums[1])
print(output)


# --------------------- Part 2 --------------------- #


data = parse_puzzle_input()
data = parse_puzzle_input(True)

all_muls = re.compile("mul\(\d+,\d+\)|do\(\)|don't\(\)", re.MULTILINE)
num_pairs = re.compile('\d+,\d+') 

output=0
run_mult = True
for pair in all_muls.findall(data):
  if pair == "do()":
    run_mult = True
    continue
  elif pair == "don't()":
    run_mult = False
    continue

  nums = num_pairs.findall(pair)[0].split(",")
  if run_mult:
    output += int(nums[0]) * int(nums[1])
print(output)

