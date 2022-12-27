#!/usr/bin/env python3
from data import data

#data = [[(498,4), (498,6), (496,6)], [(503,4), (502,4), (502,9), (494,9)]]
#
#
#my_map = {}
#min_x = min([min([j[0] for j in i]) for i in data])
#max_x = max([max([j[0] for j in i]) for i in data])
#min_y = min([min([j[1] for j in i]) for i in data])
#max_y = max([max([j[1] for j in i]) for i in data])
#
#
#def print_map():
#  global my_map, max_y, min_x, max_x
#  for i in range(max_y+1):
#    print("{} -> ".format(i), end="")
#    for j in range(min_x-1, max_x+1):
#      print(my_map["{}-{}".format(j,i)], end="")
#    print()
#
#
#for x in range(min_x-1, max_x+1):
#  for y in range(0, max_y+1):
#    my_map["{}-{}".format(x,y)] = '.'
#
#for d in data:
#  last_point = d[0]
#  my_map["{}-{}".format(d[0],d[1])] = '#'
#  for point in d[1:]:
#    if point[0] == last_point[0]:
#      x = last_point[1]
#      y = point[1]
#      change = change = -1 if x > y else 1
#      for i in range(x, y+change, change):
#        my_map["{}-{}".format(point[0],i)] = '#'
#    else:
#      x = last_point[0]
#      y = point[0]
#      change = change = -1 if x > y else 1
#      for i in range(x, y+change, change):
#        my_map["{}-{}".format(i,point[1])] = '#'
#    last_point = point
#  
#    
#
#print(min_x, max_x, min_y, max_y)
#print_map()
#
#origin = (500,0)
#done=False
#step=-1
#while not done:
#  step += 1
#  sand_stopped = False
#  sand_loc = origin
#  while not sand_stopped:
#    if sand_loc[1] == max_y:
#      done = True
#      break
#
#    next_loc = (sand_loc[0], sand_loc[1]+1)
#    if my_map["{}-{}".format(next_loc[0], next_loc[1])] == '.':
#      sand_loc = next_loc
#      continue
#    
#    next_loc = (sand_loc[0]-1, sand_loc[1]+1)
#    if my_map["{}-{}".format(next_loc[0], next_loc[1])] == '.':
#      sand_loc = next_loc
#      continue
#
#    next_loc = (sand_loc[0]+1, sand_loc[1]+1)
#    if my_map["{}-{}".format(next_loc[0], next_loc[1])] == '.':
#      sand_loc = next_loc
#      continue
#
#    my_map["{}-{}".format(sand_loc[0], sand_loc[1])] = 'o'
#    sand_stopped = True
#  
#
#print('-'*100)
#print_map()
#print(step)

# --------------------- Part 2 --------------------- #

#data = [[(498,4), (498,6), (496,6)], [(503,4), (502,4), (502,9), (494,9)]]


my_map = {}
min_x = min([min([j[0] for j in i]) for i in data])
max_x = max([max([j[0] for j in i]) for i in data])
min_y = min([min([j[1] for j in i]) for i in data])
max_y = max([max([j[1] for j in i]) for i in data])


def print_map():
  global my_map, max_y, min_x, max_x
  for i in range(max_y+3):
    print("{} -> ".format(i), end="")
    for j in range(0, 1000):
      print(my_map["{}-{}".format(j,i)], end="")
    print()


for x in range(0, 1000):
  for y in range(0, max_y+3):
    my_map["{}-{}".format(x,y)] = '.'

for d in data:
  last_point = d[0]
  my_map["{}-{}".format(d[0],d[1])] = '#'
  for point in d[1:]:
    if point[0] == last_point[0]:
      x = last_point[1]
      y = point[1]
      change = change = -1 if x > y else 1
      for i in range(x, y+change, change):
        my_map["{}-{}".format(point[0],i)] = '#'
    else:
      x = last_point[0]
      y = point[0]
      change = change = -1 if x > y else 1
      for i in range(x, y+change, change):
        my_map["{}-{}".format(i,point[1])] = '#'
    last_point = point
  
for i in range(0,1000):
  my_map["{}-{}".format(i,max_y+2)] = '#'

print(min_x, max_x, min_y, max_y)

origin = (500,0)
done=False
step=0
while not done:
  step += 1
  sand_stopped = False
  sand_loc = origin
  while not sand_stopped:
    next_loc = (sand_loc[0], sand_loc[1]+1)
    if my_map["{}-{}".format(next_loc[0], next_loc[1])] == '.':
      sand_loc = next_loc
      continue
    
    next_loc = (sand_loc[0]-1, sand_loc[1]+1)
    if my_map["{}-{}".format(next_loc[0], next_loc[1])] == '.':
      sand_loc = next_loc
      continue

    next_loc = (sand_loc[0]+1, sand_loc[1]+1)
    if my_map["{}-{}".format(next_loc[0], next_loc[1])] == '.':
      sand_loc = next_loc
      continue

    my_map["{}-{}".format(sand_loc[0], sand_loc[1])] = 'o'
    if sand_loc == origin:
      done=True
    sand_stopped = True
  

print('-'*100)
print(step)

