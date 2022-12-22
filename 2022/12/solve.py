#!/usr/bin/env python3
from data import data
import sys
sys.setrecursionlimit(7020)

#data = ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]

#start_height=83
#stop_height=69
#max_distance = len("".join(data))
#data = [[{ "height" : ord(j), "min_step" : max_distance, "steps" : None } for j in i] for i in data]
#
#def runner(current_loc, current_steps):
#  global data
#  #print(current_loc)
#  d_steps = data[current_loc[1]][current_loc[0]]["steps"]
#  if d_steps == None or len(d_steps) > len (current_steps):
#    data[current_loc[1]][current_loc[0]]["steps"] = current_steps
#  else:
#    return
#
#  #N
#  next_pos = (current_loc[0], current_loc[1]+1)
#  if next_pos[1] < len(data) and data[next_pos[1]][next_pos[0]]["height"] - 1 <= data[current_loc[1]][current_loc[0]]["height"]:
#    runner(next_pos, current_steps + [next_pos])
#
#  #S
#  next_pos = (current_loc[0], current_loc[1]-1)
#  if next_pos[1] >= 0 and data[next_pos[1]][next_pos[0]]["height"] - 1 <= data[current_loc[1]][current_loc[0]]["height"]:
#    runner(next_pos, current_steps + [next_pos])
#
#  #E
#  next_pos = (current_loc[0]+1, current_loc[1])
#  if next_pos[0] < len(data[0]) and data[next_pos[1]][next_pos[0]]["height"] - 1 <= data[current_loc[1]][current_loc[0]]["height"]:
#    runner(next_pos, current_steps + [next_pos])
#
#  #W
#  next_pos = (current_loc[0]-1, current_loc[1])
#  if next_pos[0] >= 0 and data[next_pos[1]][next_pos[0]]["height"] - 1 <= data[current_loc[1]][current_loc[0]]["height"]:
#    runner(next_pos, current_steps + [next_pos])
#
#  return
#
#start = (0,0)
#stop = (0,0)
#_y = len(data)-1 
#for i in data:
#  _x = 0
#  for j in i:
#    if j["height"] == stop_height:
#      stop = (_x,_y)
#      j["height"] = ord('z')
#      j["stop"] = True
#    if j["height"] == start_height:
#      start = (_x,_y)
#      j["height"] = ord('a')
#      j["start"] = True
#    _x+=1
#  _y-=1
#
#print(start,stop)
#
#data = data[::-1]
#runner(start, [])
#data = data[::-1]
#
#prnt_str = "{:6}"
#for _ in data:
#  for __ in _:
#    info = len(__["steps"] if __["steps"] != None else "?")
#    pre = chr(__["height"])
#    if "start" in __:
#      pre = 'S'
#    if "stop" in __:
#      pre = 'E'
#    print(prnt_str.format(pre + str(info)), end="")
#  print()

# --------------------- Part 2 --------------------- #

start_height=83
stop_height=69
max_distance = len("".join(data))
data = [[{ "height" : ord(j), "min_step" : max_distance, "steps" : None } for j in i] for i in data]

def runner(current_loc, current_steps):
  global data
  #print(current_loc)
  d_steps = data[current_loc[1]][current_loc[0]]["steps"]
  if d_steps == None or len(d_steps) > len (current_steps):
    data[current_loc[1]][current_loc[0]]["steps"] = current_steps
  else:
    return

  #N
  next_pos = (current_loc[0], current_loc[1]+1)
  if next_pos[1] < len(data) and data[next_pos[1]][next_pos[0]]["height"] + 1 >= data[current_loc[1]][current_loc[0]]["height"]:
    runner(next_pos, current_steps + [next_pos])

  #S
  next_pos = (current_loc[0], current_loc[1]-1)
  if next_pos[1] >= 0 and data[next_pos[1]][next_pos[0]]["height"] +1 >= data[current_loc[1]][current_loc[0]]["height"]:
    runner(next_pos, current_steps + [next_pos])

  #E
  next_pos = (current_loc[0]+1, current_loc[1])
  if next_pos[0] < len(data[0]) and data[next_pos[1]][next_pos[0]]["height"] + 1 >= data[current_loc[1]][current_loc[0]]["height"]:
    runner(next_pos, current_steps + [next_pos])

  #W
  next_pos = (current_loc[0]-1, current_loc[1])
  if next_pos[0] >= 0 and data[next_pos[1]][next_pos[0]]["height"] + 1 >= data[current_loc[1]][current_loc[0]]["height"]:
    runner(next_pos, current_steps + [next_pos])

  return

start = (0,0)
stop = (0,0)
_y = len(data)-1 
for i in data:
  _x = 0
  for j in i:
    if j["height"] == stop_height:
      stop = (_x,_y)
      j["height"] = ord('z')
      j["stop"] = True
    if j["height"] == start_height:
      start = (_x,_y)
      j["height"] = ord('a')
      j["start"] = True
    _x+=1
  _y-=1

print(start,stop)

data = data[::-1]
runner(stop, [])
data = data[::-1]

prnt_str = "{:6}"
for _ in data:
  for __ in _:
    info = len(__["steps"] if __["steps"] != None else "?")
    pre = chr(__["height"])
    if "start" in __:
      pre = 'S'
    if "stop" in __:
      pre = 'E'
    print(prnt_str.format(pre + str(info)), end="")
  print()
