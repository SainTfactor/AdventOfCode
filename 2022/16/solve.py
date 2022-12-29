#!/usr/bin/env python3
from data import data

data = {
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

decide_target(start_point, 30)
for step in range(30):
  pass

# --------------------- Part 2 --------------------- #

