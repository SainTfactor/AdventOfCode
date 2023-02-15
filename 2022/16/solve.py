#!/usr/bin/env python3
from itertools import permutations, combinations
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

def get_max(nodes, steps):
  global data
  ret_val = 0
  for i in nodes:
    ret_val += data[i]['rate']*steps
  return ret_val

def new_item(old_item, next_step, distance=-1):
  global data
  ret_val = {}

  if distance == -1:
    distance=get_distance(old_item['stop_point'], next_step)
  if distance > old_item['steps_remaining']:
    ret_val['path'] = old_item['path']
    ret_val['steps_remaining'] = 0
    ret_val['flow_rate'] = old_item['flow_rate']
    ret_val['current_output'] = old_item['current_output'] + (old_item['flow_rate'] * old_item['steps_remaining'])
    ret_val['stop_point'] = old_item['stop_point']
    ret_val['done'] = True
  else:
    ret_val['path'] = old_item['path'] + [next_step]
    ret_val['steps_remaining'] = old_item['steps_remaining'] - distance - 1
    ret_val['flow_rate'] = old_item['flow_rate'] + data[next_step]['rate']
    ret_val['current_output'] = old_item['current_output'] + (old_item['flow_rate'] * (distance + 1))
    ret_val['stop_point'] = next_step
    ret_val['done'] = False 
  return ret_val

def calculate_value(item):
  global data, good_valves
  ret_val = item['current_output']
  ret_val += item['flow_rate'] * item['steps_remaining']
  remaining_valves = [i for i in good_valves if not i in item['path']]
  over_on_remaining = sum(data[i]['rate'] * item['steps_remaining'] for i in remaining_valves)
  ret_val += int(over_on_remaining*0.5)
  return ret_val
  

current_max=0
good_path=None
working_solves=[{ 'path' : [], 'done' : False, 'steps_remaining' : 30, 'flow_rate' : 0, 'current_output' : 0, 'stop_point' : start_point }]
done = False
count=0
width=50
while not done:
  print(count)
  count += 1
  done=True
  new_solves = []
  for ws in working_solves:
    if len(ws['path']) == len(good_valves):
      new_step = new_item(ws, 'AA', 1000)
      if new_step['current_output'] > current_max:
        current_max = new_step['current_output']
        good_path = new_step
    else:
      for gd in good_valves:
        if not gd in ws['path']:
          done=False
          new_step = new_item(ws, gd)
          #print(new_step)
          if new_step['done']:
            if new_step['current_output'] > current_max:
              current_max = new_step['current_output']
              good_path = new_step
          else:
            new_solves.append(new_step)
        
  working_solves = sorted(new_solves, key=calculate_value, reverse=True)[0:width]
 
print(good_path) 
print(current_max)

# --------------------- Part 2 --------------------- #

