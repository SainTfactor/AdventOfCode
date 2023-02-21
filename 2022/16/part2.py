#!/usr/bin/env python3
from itertools import permutations, combinations
import sys
from data import data


# 1707
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

for d in data:
  data[d]["opened"] = False

start_point = "AA"
good_valves = [i for i in data if data[i]["rate"] > 0]

print(good_valves)

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

def new_item(old_item, next_step_a, next_step_b, stop=False):
  global data
  ret_val = {}

  if stop:
    distance_a=1000000
    distance_b=1000000
  else:
    distance_a=get_distance(old_item['stop_point_a'], next_step_a)
    distance_b=get_distance(old_item['stop_point_b'], next_step_b)

  if next_step_a in old_item['path']:
    ret_val['path'] = old_item['path']
    ret_val['steps_remaining_a'] = old_item['steps_remaining_a']
    ret_val['flow_rate_a'] = old_item['flow_rate_a']
    ret_val['current_output_a'] = old_item['current_output_a']
    ret_val['stop_point_a'] = old_item['stop_point_a']
    ret_val['done_a'] = old_item['done_a']
  elif distance_a > old_item['steps_remaining_a']:
    ret_val['path'] = old_item['path']
    ret_val['steps_remaining_a'] = 0
    ret_val['flow_rate_a'] = old_item['flow_rate_a']
    ret_val['current_output_a'] = old_item['current_output_a'] + (old_item['flow_rate_a'] * old_item['steps_remaining_a'])
    ret_val['stop_point_a'] = old_item['stop_point_a']
    ret_val['done_a'] = True
  else:
    ret_val['path'] = old_item['path'] + [next_step_a]
    ret_val['steps_remaining_a'] = old_item['steps_remaining_a'] - distance_a - 1
    ret_val['flow_rate_a'] = old_item['flow_rate_a'] + data[next_step_a]['rate']
    ret_val['current_output_a'] = old_item['current_output_a'] + (old_item['flow_rate_a'] * (distance_a + 1))
    ret_val['stop_point_a'] = next_step_a
    ret_val['done_a'] = False

  if next_step_b in old_item['path']:
    ret_val['path'] = ret_val['path']
    ret_val['steps_remaining_b'] = old_item['steps_remaining_b']
    ret_val['flow_rate_b'] = old_item['flow_rate_b']
    ret_val['current_output_b'] = old_item['current_output_b']
    ret_val['stop_point_b'] = old_item['stop_point_b']
    ret_val['done_b'] = old_item['done_b']
  elif distance_b > old_item['steps_remaining_b']:
    ret_val['path'] = ret_val['path']
    ret_val['steps_remaining_b'] = 0
    ret_val['flow_rate_b'] = old_item['flow_rate_b']
    ret_val['current_output_b'] = old_item['current_output_b'] + (old_item['flow_rate_b'] * old_item['steps_remaining_b'])
    ret_val['stop_point_b'] = old_item['stop_point_b']
    ret_val['done_b'] = True
  else:
    ret_val['path'] = ret_val['path'] + [next_step_b]
    ret_val['steps_remaining_b'] = old_item['steps_remaining_b'] - distance_b - 1
    ret_val['flow_rate_b'] = old_item['flow_rate_b'] + data[next_step_b]['rate']
    ret_val['current_output_b'] = old_item['current_output_b'] + (old_item['flow_rate_b'] * (distance_b + 1))
    ret_val['stop_point_b'] = next_step_b
    ret_val['done_b'] = False
  
  return ret_val

def calculate_value(item):
  global data, good_valves
  ret_val = item['current_output_a'] + item['current_output_b']
  ret_val += (item['flow_rate_a'] * item['steps_remaining_a']) + (item['flow_rate_b'] * item['steps_remaining_b'])
  remaining_valves = [i for i in good_valves if not i in item['path']]
  over_on_remaining = sum([data[i]['rate'] * int((item['steps_remaining_a'] + item['steps_remaining_b'])/2) for i in remaining_valves])
  ret_val += int(over_on_remaining*0.5)
  return ret_val
  

current_max=0
good_path=None
working_solves=[{ 'path' : [], 'done_a' : False, 'done_b' : False, 'steps_remaining_a' : 26, 'steps_remaining_b' : 26, 'flow_rate_a' : 0, 'flow_rate_b': 0, 'current_output_a' : 0, 'current_output_b': 0, 'stop_point_a' : start_point, 'stop_point_b' : start_point }]
done = False
count=0
width=50

print('-'*50+'\n')
while not done:
  print(count)
  print(good_path) 
  print(current_max)
  try:
    print(working_solves[0])
    print(working_solves[-1])
  except:
    pass
  print('-'*50+'\n')
  count += 1
  done=True
  new_solves = []
  for ws in working_solves:
    if len(ws['path']) == len(good_valves):
      new_step = new_item(ws, 'AA', 'AA', True)
      if (new_step['current_output_a'] + new_step['current_output_b']) > current_max:
        current_max = new_step['current_output_a'] + new_step['current_output_b']
        good_path = new_step
    else:
      some_valves = [i for i in good_valves if not i in ws['path']]
      for gda in some_valves:
        for gdb in [i for i in some_valves if i != gda]:
          if (not gda in ws['path'] and not ws['done_a']) or (not gdb in ws['path'] and not ws['done_b']):
            done=False
            new_step = new_item(ws, gda, gdb)
            #print(new_step)
            if new_step['done_a'] and new_step['done_b']:
              if (new_step['current_output_a'] + new_step['current_output_b']) > current_max:
                current_max = new_step['current_output_a'] + new_step['current_output_b'] 
                good_path = new_step
            else:
              new_solves.append(new_step)
        
  working_solves = sorted(new_solves, key=calculate_value, reverse=True)
  working_solves = working_solves[0:width]
 
print(good_path) 
print(current_max)

