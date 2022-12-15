#!/usr/bin/env python3
from data import data

#data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" #7 #19
#data = "bvwbjplbgvbhsrlpgdmjqwftvncz" #5 #23
#data = "nppdvjthqldpwncqszvftbrmjlhg" #6 #23
#data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" #10 #29
#data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" #11 #26

for i in range(len(data)-4):
  if len(set(data[i:i+4])) == 4:
    #print(data[i:i+4])
    print(i+4)
    break

# --------------------- Part 2 --------------------- #

for i in range(len(data)-14):
  if len(set(data[i:i+14])) == 14:
    #print(data[i:i+4])
    print(i+14)
    break

