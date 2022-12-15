#!/usr/bin/env python3
from processor import Processor
from data import data

data = ["$ cd /", "$ ls", "dir a", "14848514 b.txt", "8504156 c.dat", "dir d", "$ cd a", "$ ls", "dir e", "29116 f", "2557 g", "62596 h.lst", "$ cd e", "$ ls", "584 i", "$ cd ..", "$ cd ..", "$ cd d", "$ ls", "4060174 j", "8033020 d.log", "5626152 d.ext", "7214296 k"]

p = Processor(data)
#p.print_dir_tree()
#print('-'*100)
sizes = p.get_directory_sizes()
out = 0
for i in sizes:
  if sizes[i] <= 100000:
    out += sizes[i]

print(out)

# --------------------- Part 2 --------------------- #

current_free = 70000000 - sizes['/']
needed = 30000000 - current_free

can_kill = 10000000000000000
who_kill = ''
for i in sizes:
  if sizes[i] >= needed and sizes[i] <= can_kill:
    can_kill = sizes[i]
    who_kill = i

print("{} - {}".format(who_kill, can_kill))
