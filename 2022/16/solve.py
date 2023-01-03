#!/usr/bin/env python3
from itertools import permutations
import sys
from data import data


# 1651
wdata = {
  "AA" : { "rate" : 0, "neighbors" : [ "DD", "II", "BB" ] },
  "BB" : { "rate" : 13, "neighbors" : [ "CC", "AA" ] },
  "CC" : { "rate" : 2, "neighbors" : [ "DD", "BB" ] },
  "DD" : { "rate" : 20, "neighbors" : [ "CC", "AA", "EE" ] },
  "EE" : { "rate" : 3, "neighbors" : [ "FF", "DD" ] },
  "FF" : { "rate" : 0, "neighbors" : [ "EE", "GG" ] },
  "GG" : { "rate" : 0, "neighbors" : [ "FF", "HH" ] },
  "HH" : { "rate" : 22, "neighbors" : [ "GG" ] },
  "II" : { "rate" : 0, "neighbors" : [ "AA", "JJ" ] },
  "JJ" : { "rate" : 21, "neighbors" : [ "II" ] }
}

# 607
wdata = {
  "AA" : { "rate" : 0, "neighbors" : [ "BB", "CC", "DD" ] },
  "BB" : { "rate" : 1, "neighbors" : [ "AA" ] },
  "CC" : { "rate" : 1, "neighbors" : [ "AA" ] },
  "DD" : { "rate" : 20, "neighbors" : [ "AA" ] }
}


for d in data:
  data[d]["opened"] = False

start_point = "AA"
good_valves = [i for i in data if data[i]["rate"] > 0]

def get_distance(point_a, point_b, distance=1,tried=[]):
  global data
  ret_val = 100
  for i in [j for j in data[point_a]["neighbors"] if not j in tried]:
    if i == point_b:
      ret_val = distance if distance < ret_val else ret_val
    else:
      temp_ret_val = get_distance(i, point_b, distance + 1, tried + [i])
      ret_val = temp_ret_val if temp_ret_val < ret_val else ret_val
  return ret_val

def decide_target(current_loc, remaining_time):
  global data, good_valves
  best_value = 0
  for gv in good_valves:
    pot_value = (remaining_time - get_distance(current_loc, gv)) * data[gv]["rate"]
    print("AA to {}: {}".format(gv, pot_value))

def process(good_valves, start_point, steps_left=30):
  global data
  turns = permutations(good_valves)
  
  biggest=0
  best_steps=0
  route = None
  for tgts in turns:
    current_loc = start_point
    steps = steps_left
    output = 0
    for step in tgts:
      dst = get_distance(current_loc, step)
      #print("{}, {}, {}".format(current_loc, step, dst))
      steps -= dst + 1
      if steps < 0:
        break
      output += steps*data[step]["rate"]
      current_loc = step
      #print("{}, {}, {}".format(30 - steps + 1, data[step]["rate"], output))
    #print("{} - {}".format(tgts, output))
    if biggest < output or (biggest == output and steps > best_steps):
      biggest = output
      best_steps = steps
      route = tgts
  return (biggest, route, best_steps if best_steps > 0 else 0)

rate_range = sorted([data[i]["rate"] for i in data if data[i]["rate"] != 0])

#split_point = int(sys.argv[1])
range_1 = rate_range[12:]
range_2 = rate_range[8:12]
range_3 = rate_range[4:8]
range_4 = rate_range[0:4]
print(range_1, range_2, range_3, range_4)

print("-"*100)
b1, r1, steps_left = process([i for i in good_valves if data[i]["rate"] in range_1], start_point)
print(b1, r1, steps_left)
print("-"*100)
b2, r2, steps_left = process([i for i in good_valves if data[i]["rate"] in range_2], r1[-1], steps_left)
print(b2, r2, steps_left)
print("-"*100)
b3, r3, steps_left = process([i for i in good_valves if data[i]["rate"] in range_3], r2[-1], steps_left)
print(b3, r3, steps_left)
print("-"*100)
b4, r4, steps_left = process([i for i in good_valves if data[i]["rate"] in range_4], r3[-1], steps_left)
print(b4, r4, steps_left)
print("-"*100)

print("="*100)
print(b1+b2+b3+b4)
# --------------------- Part 2 --------------------- #

