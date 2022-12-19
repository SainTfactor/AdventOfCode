#!/usr/bin/env python3
from data import data

#data = ["addx 15", "addx -11", "addx 6", "addx -3", "addx 5", "addx -1", "addx -8", "addx 13", "addx 4", "noop", "addx -1", "addx 5", "addx -1", "addx 5", "addx -1", "addx 5", "addx -1", "addx 5", "addx -1", "addx -35", "addx 1", "addx 24", "addx -19", "addx 1", "addx 16", "addx -11", "noop", "noop", "addx 21", "addx -15", "noop", "noop", "addx -3", "addx 9", "addx 1", "addx -3", "addx 8", "addx 1", "addx 5", "noop", "noop", "noop", "noop", "noop", "addx -36", "noop", "addx 1", "addx 7", "noop", "noop", "noop", "addx 2", "addx 6", "noop", "noop", "noop", "noop", "noop", "addx 1", "noop", "noop", "addx 7", "addx 1", "noop", "addx -13", "addx 13", "addx 7", "noop", "addx 1", "addx -33", "noop", "noop", "noop", "addx 2", "noop", "noop", "noop", "addx 8", "noop", "addx -1", "addx 2", "addx 1", "noop", "addx 17", "addx -9", "addx 1", "addx 1", "addx -3", "addx 11", "noop", "noop", "addx 1", "noop", "addx 1", "noop", "noop", "addx -13", "addx -19", "addx 1", "addx 3", "addx 26", "addx -30", "addx 12", "addx -1", "addx 3", "addx 1", "noop", "noop", "noop", "addx -9", "addx 18", "addx 1", "addx 2", "noop", "noop", "addx 9", "noop", "noop", "noop", "addx -1", "addx 2", "addx -37", "addx 1", "addx 3", "noop", "addx 15", "addx -21", "addx 22", "addx -6", "addx 1", "noop", "addx 2", "addx 1", "noop", "addx -10", "noop", "noop", "addx 20", "addx 1", "addx 2", "addx 2", "addx -6", "addx -11", "noop", "noop", "noop"]



#X=1
#cycles=0
#sig_str=0
#
#def push_cycle(add_data=None):
#  global cycles
#  global X
#  global sig_str
#  cycles += 1
#
#  if (cycles - 20) % 40 == 0:
#    sig_str += (cycles * X)
#
#  if not add_data == None:
#    X += add_data
#
#for instruction in data:
#  if instruction[0:4] == "noop":
#    push_cycle()
#  elif instruction[0:4] == "addx":
#    push_cycle()
#    push_cycle(int(instruction[5:]))
#
#print(sig_str)

# --------------------- Part 2 --------------------- #

X=1
cycles=0
sig_str=0

output = ""

def push_cycle(add_data=None):
  global cycles
  global X
  global sig_str
  global output

  print(cycles,X)
  output += "#" if (cycles%40 >= X-1 and cycles%40 <= X+1) else "."
  
  cycles += 1
  if not add_data == None:
    X += add_data

for instruction in data:
  if instruction[0:4] == "noop":
    push_cycle()
  elif instruction[0:4] == "addx":
    push_cycle()
    push_cycle(int(instruction[5:]))


cnt=0
for i in output:
  if cnt%40 == 0:
    print()
  print(i, end="")
  cnt += 1
print()
print()



