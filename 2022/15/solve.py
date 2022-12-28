#!/usr/bin/env python3
from data import data

#data = [[(2,18), (-2,15)], [(9,16), (10,16)], [(13,2), (15,3)], [(12,14), (10,16)], [(10,20), (10,16)], [(14,17), (10,16)], [(8,7), (2,10)], [(2,0), (2,10)], [(0,11), (2,10)], [(20,14), (25,17)], [(17,20), (21,22)], [(16,7), (15,3)], [(14,3), (15,3)], [(20,1), (15,3)]]

def range_reduce(ranges, bounds=[]):
  min_start = min([i[0] for i in ranges])
  max_end   = max([i[1] for i in ranges]) + 1
  if len(bounds) != 0:
    min_start = max([min_start, bounds[0]])
    max_end   = min([max_end,   bounds[1] + 1])
  outy_a = [range(i[0] if i[0] > min_start else min_start, i[1] + 1 if i[1] < max_end else max_end) for i in ranges]
  outy = set([outval for inval in outy_a for outval in inval])
  #print(outy)
  return outy

def widths_at_ys(target_y, between=[], count_beacons=False):
  widths_at_centers={}
  sides_at_centers={}
  for i in data:
    distance = abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1])
    width_at_origin = (2*distance) + 1
    vert_distance = abs(target_y - i[0][1])
    width_at_line = max([0, width_at_origin - (2*vert_distance)])
    if i[0][0] in widths_at_centers:
      widths_at_centers[i[0][0]] = max([widths_at_centers[i[0][0]], width_at_line])
      sides_at_centers[i[0][0]] = max([int((sides_at_centers[i[0][0]]-1)/2), int((width_at_line-1)/2)])
    else:
      widths_at_centers[i[0][0]] = width_at_line
      sides_at_centers[i[0][0]] = int((width_at_line-1)/2)
  hits = {}
  ranges=[]
  for i in widths_at_centers:
    if widths_at_centers[i] == 0:
      continue
    start = i-sides_at_centers[i]
    stop = i+sides_at_centers[i]
    ranges.append((start, stop))
  if len(between) == 0:
    num_covered = len(range_reduce(ranges))
  else:
    covered = range_reduce(ranges, between)
    num_covered = len(covered)
  beacons_covered = set([i[1] for i in data if i[1][1] == target_y and i[1][0] in hits])
  return num_covered - (len(beacons_covered) if not count_beacons else 0)

#print(widths_at_ys(10))
#print(widths_at_ys(2000000))

# --------------------- Part 2 --------------------- #

stop_point = 0
# return true if full range covered
def check_coverage(ranges, min_val, max_val):
  global stop_point
  stop = min_val
  found = False
  while not found:
    found = True
    for r in ranges:
      if r[0] <= stop + 1 and r[1] > stop:
        stop = r[1]
        found = False
      if stop >= max_val:
        return True
  stop_point = stop + 1
  return False
      
def covers_all(target_y, between=[], count_beacons=False):
  widths_at_centers={}
  sides_at_centers={}
  for i in data:
    distance = abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1])
    width_at_origin = (2*distance) + 1
    vert_distance = abs(target_y - i[0][1])
    width_at_line = max([0, width_at_origin - (2*vert_distance)])
    if i[0][0] in widths_at_centers:
      widths_at_centers[i[0][0]] = max([widths_at_centers[i[0][0]], width_at_line])
      sides_at_centers[i[0][0]] = max([int((sides_at_centers[i[0][0]]-1)/2), int((width_at_line-1)/2)])
    else:
      widths_at_centers[i[0][0]] = width_at_line
      sides_at_centers[i[0][0]] = int((width_at_line-1)/2)
  hits = {}
  ranges=[]
  for i in widths_at_centers:
    if widths_at_centers[i] == 0:
      continue
    start = i-sides_at_centers[i]
    stop = i+sides_at_centers[i]
    ranges.append((start, stop))
  covered = check_coverage(ranges, between[0], between[1])
  return covered

print('-'*100)
h=4000000

#data = [[(2,18), (-2,15)], [(9,16), (10,16)], [(13,2), (15,3)], [(12,14), (10,16)], [(10,20), (10,16)], [(14,17), (10,16)], [(8,7), (2,10)], [(2,0), (2,10)], [(0,11), (2,10)], [(20,14), (25,17)], [(17,20), (21,22)], [(16,7), (15,3)], [(14,3), (15,3)], [(20,1), (15,3)]]
#h=20

# bad_width  = 4000001
# good_width = 4000000

output_val = None
for i in range(h+1):
  if i % 1000 == 0:
    print("{}/{}".format(i,h))
  covered = covers_all(i, [0,h], True)
  #print(width)
  if not covered:
    output_val = i
    break 

print(stop_point, output_val)
print((stop_point*4000000)+output_val)
