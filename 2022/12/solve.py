#!/usr/bin/env python3
from data import data

data = ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]

start_height=83
stop_height=69
max_distance = len("".join(data))
data = [[{ "height" : ord(j), "min_step" : max_distance, "steps" : None } for j in i] for i in data]

def runner(current_loc, current_steps):
  runner(current_loc, current_steps)

start = (0,0)
stop = (0,0)
_y = len(data)-1 
for i in data:
  _x = 0
  for j in i:
    if j["height"] == stop_height:
      stop = (_x,_y)
      j["height"] == ord('z')
    if j["height"] == start_height:
      start = (_x,_y)
      j["height"] == ord('a')
    _x+=1
  _y-=1

#runner()
print(start,stop)

# --------------------- Part 2 --------------------- #

