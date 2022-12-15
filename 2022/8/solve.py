#!/usr/bin/env python3
from data import data

#data = [ "30373", "25512", "65332", "33549", "35390" ]

def is_vis(r,c):
  global data
  vN,vS,vE,vW = True,True,True,True
  height = data[r][c]
  #N
  for i in range(1, r+1):
    if height <= data[r-i][c]:
      vN = False
  #S
  for i in range(1, len(data)-r):
    if height <= data[r+i][c]:
      vS = False
  #W
  for i in range(1, c+1):
    if height <= data[r][c-i]:
      vW = False
  #E
  for i in range(1, len(data[0])-c):
    if height <= data[r][c+i]:
      vE = False
  #print("row: {}, col: {}, vN: {}, vS: {}, vE: {}, vW: {}".format(r,c,vN,vS,vE,vW))
  return vN or vS or vE or vW

#print('\n'.join(data))

outcnt=(len(data)*2) + ((len(data)-2)*2)
for row in range(1, len(data) - 1):
  for col in range(1, len(data) - 1):
    #print("row: {}, col: {}, val: {}".format(row, col, data[row][col]))
    if is_vis(row, col):
      outcnt += 1
print(outcnt)

# --------------------- Part 2 --------------------- #

def area_seen(r,c):
  global data
  vN,vS,vE,vW = 0,0,0,0
  height = data[r][c]
  #N
  for i in range(1, r+1):
    vN += 1
    if height <= data[r-i][c]:
      break
  #S
  for i in range(1, len(data)-r):
    vS += 1
    if height <= data[r+i][c]:
      break
  #W
  for i in range(1, c+1):
    vW += 1
    if height <= data[r][c-i]:
      break
  #E
  for i in range(1, len(data[0])-c):
    vE += 1
    if height <= data[r][c+i]:
      break
  #print("row: {}, col: {}, vN: {}, vS: {}, vE: {}, vW: {}".format(r,c,vN,vS,vE,vW))
  return vN * vS * vE * vW


biggest_area=0
for row in range(1, len(data) - 1):
  for col in range(1, len(data) - 1):
    #print("row: {}, col: {}, val: {}".format(row, col, data[row][col]))
    new_area = area_seen(row, col)
    if new_area > biggest_area:
      biggest_area = new_area
print(biggest_area)


