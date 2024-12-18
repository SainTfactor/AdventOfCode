#!/usr/bin/env python3
import re
import argparse

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  probs = []

  def get_coords(string):
    numchk = re.compile("[^\d]+(\d+)[^\d]+(\d+)")
    groups = numchk.search(string).groups()
    return (int(groups[0]), int(groups[1]))

  prob = {}
  for i in data:
    if i == "":
      probs.append(prob)
      prob = {}
    if "A:" in i:
      prob["A"] = get_coords(i)
    if "B:" in i:
      prob["B"] = get_coords(i)
    if "Prize:" in i:
      prob["Goal"] = get_coords(i)

  probs.append(prob)
  return probs



def math_intersection(prob):
  one = prob["A"][1]
  two = prob["B"][1]
  three = prob["Goal"][1]
  four = prob["A"][0]
  five = prob["B"][0]
  six = prob["Goal"][0]
  B = (four*three - one*six)/(four*two - one*five)
  A = (three - two*B)/one
  return A,B


if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  data = parse_puzzle_input(args.real)
 
  output = 0
  for i in data:
    a,b = math_intersection(i)
    if int(a) == a:
      output += int(3*a + b)

  print(output)

  # --------------------- Part 2 --------------------- #

  data = parse_puzzle_input(args.real)

  for i in data:
    x = i["Goal"][0] + 10000000000000
    y = i["Goal"][1] + 10000000000000
    i["Goal"] = (x,y)

  output = 0
  for i in data:
    a,b = math_intersection(i)
    if int(a) == a and int(b) == b:
      output += int(3*a + b)

  print(output)


