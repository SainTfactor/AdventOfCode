#!/usr/bin/env python3
import argparse

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  def cleaner(line):
    split_val = line.split(": ")
    target = int(split_val[0])
    operands = [int(i) for i in split_val[1].split(" ")]
    return (target, operands)

  return [cleaner(i) for i in data]






if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  args = parser.parse_args()

  data = parse_puzzle_input(args.real)

  # --------------------- Part 1 --------------------- #

  def reduce_problem(target, pieces):
    problems = []
    good = False
    new_pieces = pieces[0:-1] 
    if len(new_pieces) == 0:
      if target == pieces[-1]:
        return True
      else:
        return False

    if target % pieces[-1] == 0:
      new_target = int(target/pieces[-1]) 
      problems.append((new_target, new_pieces))
    new_target = target - pieces[-1]
    problems.append((new_target, new_pieces))

    for prob in problems:
      if reduce_problem(prob[0], prob[1]):
        return True
    return False

  output = 0
  for problem in data:
    if reduce_problem(problem[0], problem[1]):
      output += problem[0]
  print(output)




  # --------------------- Part 2 --------------------- #


  def reduce_problem(target, pieces):
    problems = []
    good = False
    new_pieces = pieces[0:-1] 
    if len(new_pieces) == 0:
      if target == pieces[-1]:
        return True
      else:
        return False
    if target < 0:
      return False

    if target % pieces[-1] == 0:
      new_target = int(target/pieces[-1]) 
      problems.append((new_target, new_pieces))

    str_tar = "{}".format(target)
    str_pce = "{}".format(pieces[-1])
    if str_tar[-len(str_pce):] == str_pce:
      str_target = str_tar[0:len(str_tar)-len(str_pce)]
      if str_target != "":
        problems.append((int(str_target), new_pieces))
    
    new_target = target - pieces[-1]
    problems.append((new_target, new_pieces))

    for prob in problems:
      if reduce_problem(prob[0], prob[1]):
        return True
    return False

  output = 0
  for problem in data:
    if reduce_problem(problem[0], problem[1]):
      output += problem[0]
  print(output)


