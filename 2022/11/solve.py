#!/usr/bin/env python3
from data import data

test_data = {
  0: {
    "items": [ 79, 98 ],
    "operation": lambda val: val * 19,
    "test": 23,
    "true": 2,
    "false": 3
  },
  1: {
    "items": [ 54, 65, 75, 74 ],
    "operation": lambda val: val + 6,
    "test": 19,
    "true": 2,
    "false": 0
  },
  2: {
    "items": [ 79, 60, 97 ],
    "operation": lambda val: val * val,
    "test": 13,
    "true": 1,
    "false": 3
  },
  3: {
    "items": [ 74 ],
    "operation": lambda val: val + 3,
    "test": 17,
    "true": 0,
    "false": 1
  }
}

#def process_monkey(monkey):
#  global data
#  manipulate_me = data[monkey]["items"]
#  for _ in range(len(manipulate_me)):
#    first_val = manipulate_me[0]
#    manipulate_me = manipulate_me[1:]
#    first_val = int(data[monkey]["operation"](first_val)/3)
#    data[monkey]["count"] += 1
#    target = data[monkey]["true"] if first_val % data[monkey]["test"] == 0 else data[monkey]["false"]
#    data[target]["items"].append(first_val)
#  data[monkey]["items"] = []
#    
#
#for m in data:
#  data[m]["count"] = 0
#for _ in range(20):
#  for monkey in data:
#    process_monkey(monkey)
#
#print(data)
#cnts = [data[i]["count"] for i in data]
#print (cnts)

# --------------------- Part 2 --------------------- #

def prod(lst):
  x=1
  for i in lst:
    x *= i
  return x


magic_number = prod([data[i]["test"] for i in data])
def process_monkey(monkey):
  global data
  global magic_number
  manipulate_me = data[monkey]["items"]
  for _ in range(len(manipulate_me)):
    first_val = manipulate_me[0]
    manipulate_me = manipulate_me[1:]
    first_val = data[monkey]["operation"](first_val)
    data[monkey]["count"] += 1
    target = data[monkey]["true"] if first_val % data[monkey]["test"] == 0 else data[monkey]["false"]
    first_val = first_val % magic_number   
 
    data[target]["items"].append(first_val)
  data[monkey]["items"] = []
    

for m in data:
  data[m]["count"] = 0
for _ in range(10000):
  for monkey in data:
    process_monkey(monkey)

print(data)
cnts = [data[i]["count"] for i in data]
print (cnts)


