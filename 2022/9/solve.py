#!/usr/bin/env python3
from data import data

#data = [("R", 4), ("U", 4), ("L", 3), ("D", 1), ("R", 4), ("D", 1), ("L", 5), ("R", 2)]

def update_tail_history(tail_pos):
  global hist_obj
  key = "{}-{}".format(tail_pos[0], tail_pos[1])
  if key in hist_obj:
    hist_obj[key] += 1
  else:
    hist_obj[key] = 1

#def move(hp, tp, move_info):
#  horz = 1 if move_info[0] == 'R' else -1 if move_info[0] == 'L' else 0
#  vert = 1 if move_info[0] == 'U' else -1 if move_info[0] == 'D' else 0
#  for i in range(move_info[1]):
#    last_hp = [hp[0],hp[1]]
#    hp[0] += horz
#    hp[1] += vert
#    if abs(hp[0] - tp[0]) > 1 or abs(hp[1] - tp[1]) > 1:
#      tp[0] = last_hp[0]
#      tp[1] = last_hp[1]
#      update_tail_history(tp)

# Revamped for part 2
def move(chain, move_info):
  horz = 1 if move_info[0] == 'R' else -1 if move_info[0] == 'L' else 0
  vert = 1 if move_info[0] == 'U' else -1 if move_info[0] == 'D' else 0
  for i in range(move_info[1]):
    hp = chain[0]
    hp[0] += horz
    hp[1] += vert
    last_link = hp
    pre_chain_end = [chain[-1][0], chain[-1][1]]
    for link in chain[1:]:
      if abs(last_link[0] - link[0]) > 1 or abs(last_link[1] - link[1]) > 1:
        link[0] = link[0] + 1 if last_link[0] > link[0] else link[0] - 1 if last_link[0] < link[0] else link[0]
        link[1] = link[1] + 1 if last_link[1] > link[1] else link[1] - 1 if last_link[1] < link[1] else link[1]
      last_link = link
    post_chain_end = [chain[-1][0], chain[-1][1]]
    if not (pre_chain_end[0] == post_chain_end[0] and pre_chain_end[1] == post_chain_end[1]):
      update_tail_history(post_chain_end)


hist_obj={ '0-0': 1 }
chain = [[0,0] for i in range(2)]
for i in data:
  move(chain, i)

#print(hist_obj)
print(len([i for i in hist_obj]))

# --------------------- Part 2 --------------------- #

def printout(chain):
  for j in range(50,0,-1):
    for i in range(50):
      occ = [i, j] in chain
      if occ:
        print(chain.index([i,j]), end="")
      else:
        print('.', end="")
    print()
  print()

#data = [("R", 5), ("U", 8), ("L", 8), ("D", 3), ("R", 17), ("D", 10), ("L", 25), ("U", 20)]
#hist_obj={ '5-11': 1 }
#chain = [[5,11] for i in range(10)]


hist_obj={ '0-0': 1 }
chain = [[0,0] for i in range(10)]
for i in data:
  move(chain, i)

#print(hist_obj)
print(len([i for i in hist_obj]))


