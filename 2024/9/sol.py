#!/usr/bin/env python3
import argparse

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()][0]

  data = [int(i) for i in data]
  return data[::2], data[1::2]




if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  args = parser.parse_args()


  # --------------------- Part 1 --------------------- #

  def feed_head(files, pointer_head, outdisk):
    while files[pointer_head] != 0:
      outdisk.append(pointer_head)
      files[pointer_head] -= 1
    return pointer_head + 1

  def feed_tail(files, spaces, pointer_tail, pointer_spaces, outdisk):
    while spaces[pointer_spaces] != 0:
      while files[pointer_tail] == 0:
        if pointer_tail == 0:
          print("Wild Bail Hitchcock")
          return 0
        pointer_tail -= 1
      outdisk.append(pointer_tail)
      files[pointer_tail] -= 1
      spaces[pointer_spaces] -= 1
    return pointer_tail

  files, spaces = parse_puzzle_input(args.real)

  outdisk = []

  pointer_head = 0
  pointer_tail = len(files) - 1
  pointer_spaces = 0
  while pointer_head < pointer_tail:
    pointer_head = feed_head(files, pointer_head, outdisk)
    pointer_tail = feed_tail(files, spaces, pointer_tail, pointer_spaces, outdisk)
    pointer_spaces += 1
  pointer_head = feed_head(files, pointer_head, outdisk)

  #print("".join([str(i) for i in outdisk]))
  #print(outdisk)
  #print("--------------------")
  chksum = 0
  counter = 0
  for i in outdisk:
    chksum += i * counter
    counter += 1
  print(chksum)

  # --------------------- Part 2 --------------------- #


  _files, _spaces = parse_puzzle_input(args.real)
  files = {}
  spaces = {}
  for f in range(len(_files)):
    files[f] = { "size" : _files[f], "moved" : False }
  for s in range(len(_spaces)):
    spaces[s] = { "size" : _spaces[s], "occupants": [], "remaining_space" : _spaces[s] }

  for f in range(len(_files)-1, 0, -1):
    for s in range(f):
      if files[f]["size"] <= spaces[s]["remaining_space"]:
        files[f]["moved"] = True
        spaces[s]["remaining_space"] = spaces[s]["remaining_space"] - files[f]["size"]
        spaces[s]["occupants"].append(f)
        break

  #for f in files:
  #  print(f,files[f])
  #print("--------")
  #for s in spaces:
  #  print(s,spaces[s])

  output = []
  for i in range(len(_spaces)):
    appender = "." if files[i]["moved"] else i
    for _ in range(files[i]["size"]):
      output.append(appender)

    for occ in spaces[i]["occupants"]:
      for f in range(files[occ]["size"]):
        output.append(occ)

    for s in range(spaces[i]["remaining_space"]):
      output.append(".")

  last_file = len(_spaces)
  appender = "." if files[last_file]["moved"] else last_file
  for _ in range(files[last_file]["size"]):
    output.append(appender)


  #print(output)
  #print("".join([str(i) for i in output]))
  chksum = 0
  counter = 0
  for i in output:
    if i != ".":
      chksum += i * counter
    counter += 1
  print(chksum)
