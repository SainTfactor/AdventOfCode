#!/usr/bin/env python3
import re
import argparse

def parse_puzzle_input(real_data, sample_data_file):
  data_source = "real_data.txt" if real_data else sample_data_file
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  nums = re.compile("\d+")
  reg_a = int(nums.findall(data[0])[0])
  reg_b = int(nums.findall(data[1])[0])
  reg_c = int(nums.findall(data[2])[0])
  prog = [int(i) for i in nums.findall(data[4])]

  return reg_a, reg_b, reg_c, prog

if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  parser.add_argument("-s", "--sample_file", default="sample_data.txt", help="Specify alternate name for sample data file.  Default: sample_data.txt")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  def combo(operand):
    global REG_A, REG_B, REG_C, INST_PNTR
    if operand <= 3:
      return operand
    if operand == 4:
      return REG_A
    if operand == 5:
      return REG_B
    if operand == 6:
      return REG_C
    raise Exception

  def adv(operand):
    global REG_A, REG_B, REG_C, INST_PNTR
    new_val = int(REG_A/(2**combo(operand)))
    REG_A = new_val
    INST_PNTR += 2
  def bxl(operand):
    global REG_A, REG_B, REG_C, INST_PNTR
    new_val = REG_B ^ operand
    REG_B = new_val
    INST_PNTR += 2
  def bst(operand):
    global REG_A, REG_B, REG_C, INST_PNTR
    new_val = combo(operand) % 8
    REG_B = new_val
    INST_PNTR += 2
  def jnz(operand):
    global REG_A, REG_B, REG_C, INST_PNTR
    if REG_A != 0:
      INST_PNTR = operand
    else:
      INST_PNTR += 2
  def bxc(operand):
    global REG_A, REG_B, REG_C, INST_PNTR
    new_val = REG_B ^ REG_C
    REG_B = new_val
    INST_PNTR += 2
  def out(operand):
    global REG_A, REG_B, REG_C, INST_PNTR, OUTPUT_BUFFER
    OUTPUT_BUFFER.append(combo(operand)%8)
    INST_PNTR += 2
  def bdv(operand):
    global REG_A, REG_B, REG_C, INST_PNTR
    new_val = int(REG_A/(2**combo(operand)))
    REG_B = new_val
    INST_PNTR += 2
  def cdv(operand):
    global REG_A, REG_B, REG_C, INST_PNTR
    new_val = int(REG_A/(2**combo(operand)))
    REG_C = new_val
    INST_PNTR += 2

  REG_A, REG_B, REG_C, PROGRAM = parse_puzzle_input(args.real, args.sample_file)
  OPCODES = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
  INST_PNTR = 0
  OUTPUT_BUFFER = []
  
  while True:
    try:
      inst, operand = PROGRAM[INST_PNTR:INST_PNTR+2]
    except:
      break

    OPCODES[inst](operand)

  print(",".join([str(i) for i in OUTPUT_BUFFER]))

  # --------------------- Part 2 --------------------- #

  test_a_val = 0
  prev_val = 0
  REG_A, oREG_B, oREG_C, PROGRAM = parse_puzzle_input(args.real, args.sample_file)
  OPCODES = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
  last_len = 0
  while True:
    REG_A = test_a_val
    REG_B = oREG_B
    REG_C = oREG_C
    INST_PNTR = 0
    OUTPUT_BUFFER = []

    while True:
      try:
        inst, operand = PROGRAM[INST_PNTR:INST_PNTR+2]
      except:
        break
      for obi in range(len(OUTPUT_BUFFER)):
        if PROGRAM[obi] != OUTPUT_BUFFER[obi]:
          break
      
      if len(OUTPUT_BUFFER) > 3 and OUTPUT_BUFFER == PROGRAM[len(PROGRAM) - len(OUTPUT_BUFFER):]:
        print("{} - {}".format(test_a_val - prev_val, test_a_val))
        prev_val = test_a_val
        break

      OPCODES[inst](operand)
      #print(inst, operand, (REG_A, REG_B, REG_C), OUTPUT_BUFFER)
      #input()
    
    #if last_len != len(OUTPUT_BUFFER):
    #  print("{}:{} -- {},{} -- {}".format(OUTPUT_BUFFER, len(OUTPUT_BUFFER), PROGRAM, len(PROGRAM), test_a_val))
    #  last_len = len(OUTPUT_BUFFER)
    if PROGRAM == OUTPUT_BUFFER:
      print(test_a_val)
      break
    else:
      test_a_val += 1

    if test_a_val % 10000 == 0:
      print(test_a_val)
