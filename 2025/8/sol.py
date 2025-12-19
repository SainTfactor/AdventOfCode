#!/usr/bin/env python3
import math
import argparse

def parse_puzzle_input(real_data, sample_data_file):
  data_source = "real_data.txt" if real_data else sample_data_file
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  # manipulate data
  def cleaner(line):
    return { "coordinates": [int(i) for i in line.split(',')], "nearest_neighs": [], "connections": [], "seen": False}

  return [cleaner(i) for i in data]



if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  parser.add_argument("-s", "--sample_file", default="sample_data.txt", help="Specify alternate name for sample data file.  Default: sample_data.txt")
  args = parser.parse_args()

  # --------------------- Part 1 --------------------- #

  data = parse_puzzle_input(args.real, args.sample_file)

  def dist_between(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

  def bottom_x_entries(mylist, comp_item, num_entries):
    output_array = [0]*num_entries
    for i in range(num_entries):
      smallest_item = mylist[0]
      smallest_distance = dist_between(comp_item["coordinates"], mylist[0]["coordinates"])
      for j in mylist[1:]:
        newdst = dist_between(comp_item["coordinates"], j["coordinates"]) 
        if newdst < smallest_distance:
          smallest_item = j
          smallest_distance = newdst
      output_array[i] = { "item" : smallest_item["coordinates"], "dst" : smallest_distance}
      mylist.remove(smallest_item)
    return output_array

  for obj in data:
    obj["nearest_neighs"] = bottom_x_entries([i for i in data if i != obj], obj, 10)
  

  def find_smallest(mylist):
    smallest = mylist[0]
    for i in mylist[1:]:
      if i["nearest_neighs"][0]["dst"] < smallest["nearest_neighs"][0]["dst"]:
        smallest = i
    return smallest

  def get_item(mylist, coords):
    for x in mylist:
      if x["coordinates"] == coords:
        return x

  done = 0
  while done < 10:
    already_tied = False
    tester = find_smallest(data)
    mate = get_item(data, tester["nearest_neighs"][0]["item"])
    tester["nearest_neighs"].remove(tester["nearest_neighs"][0])
    if mate["coordinates"] in tester["connections"]:
      continue
  
    tester["connections"].append(mate["coordinates"])
    for x in mate["connections"]:
      if not x in tester["connections"]:
        tester["connections"].append(x)

    mate["connections"].append(tester["coordinates"])
    for x in tester["connections"]:
      if not x in mate["connections"]:
        mate["connections"].append(x)
    
    done += 1
    

  for j in sorted(data, key = lambda x : len(x["connections"])):
    print("{}: {}".format(j["coordinates"], j["connections"]))

  # --------------------- Part 2 --------------------- #

  data = parse_puzzle_input(args.real, args.sample_file)



