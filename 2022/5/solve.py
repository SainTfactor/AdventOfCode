#!/usr/bin/env python3
from data import crates, moves

#crates = ["NZ", "DCM", "P"]
#moves = [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]

#for i in moves:
#  #print(i, crates)
#  dst,src,cnt = (i[2]-1),(i[1]-1),i[0]
#  crates[dst] = crates[src][0:cnt][::-1] + crates[dst]
#  crates[src] = crates[src][cnt:]
#
#print(''.join([i[0] for i in crates]))

# --------------------- Part 2 --------------------- #

for i in moves:
  dst,src,cnt = (i[2]-1),(i[1]-1),i[0]
  crates[dst] = crates[src][0:cnt] + crates[dst]
  crates[src] = crates[src][cnt:]

print(''.join([i[0] for i in crates]))
