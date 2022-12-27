#!/usr/bin/env python3
from data import data

#data = [[(2,18), (-2,15)], [(9,16), (10,16)], [(13,2), (15,3)], [(12,14), (10,16)], [(10,20), (10,16)], [(14,17), (10,16)], [(8,7), (2,10)], [(2,0), (2,10)], [(0,11), (2,10)], [(20,14), (25,17)], [(17,20), (21,22)], [(16,7), (15,3)], [(14,3), (15,3)], [(20,1), (15,3)]]

def widths_at_ys(target_y, between=[], count_beacons=False):
  widths_at_centers={}
  for i in data:
    distance = abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1])
    width_at_origin = (2*distance) + 1
    vert_distance = abs(target_y - i[0][1])
    width_at_line = max([0, width_at_origin - (2*vert_distance)])
    if i[0][0] in widths_at_centers:
      widths_at_centers[i[0][0]] = max([widths_at_centers[i[0][0]], width_at_line])
    else:
      widths_at_centers[i[0][0]] = width_at_line
    
  hits = []
  for i in widths_at_centers:
    if widths_at_centers[i] == 0:
      continue
    start = i-int((widths_at_centers[i]-1)/2)
    stop = i+int((widths_at_centers[i]-1)/2)
    for j in range(start,stop+1):
      hits.append(j)
  if len(between) == 0:
    #print(set(hits))
    num_covered = len(set(hits))
  else:
    covered = [i for i in set(hits) if i >= between[0] and i <= between[1]]
    num_covered = len(covered)
  beacons_covered = set([i[1] for i in data if i[1][1] == target_y and i[1][0] in hits])
  return num_covered - (len(beacons_covered) if not count_beacons else 0)

#print(widths_at_ys(10))
#print(widths_at_ys(2000000))

# --------------------- Part 2 --------------------- #

print('-'*100)
h=4000000

#data = [[(2,18), (-2,15)], [(9,16), (10,16)], [(13,2), (15,3)], [(12,14), (10,16)], [(10,20), (10,16)], [(14,17), (10,16)], [(8,7), (2,10)], [(2,0), (2,10)], [(0,11), (2,10)], [(20,14), (25,17)], [(17,20), (21,22)], [(16,7), (15,3)], [(14,3), (15,3)], [(20,1), (15,3)]]
#h=20

# bad_width  = 4000001
# good_width = 4000000

for i in range(h+1):
  width = widths_at_ys(i, [0,h], True)
  print(width)
 
