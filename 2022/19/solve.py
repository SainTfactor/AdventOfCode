#!/usr/bin/env python3
from data import blueprints

# Observations:
#  You never need more than the biggest cost of each type of robot, as that means you can make one of cost per turn.
#    eg. You never need more than 4 ore robots, 14 clay robots, and 7 obsidian robots in blueprint 1.  After that, just do geode robots.

bblueprints = [
  { 
    "ore_robot" : { "ore" : 4 }, 
    "clay_robot" : { "ore" : 2 }, 
    "obsidian_robot" : { "ore" : 3, "clay" : 14 }, 
    "geode_robot" :{ "ore" : 2, "obsidian" : 7 } 
  }, 
  { 
    "ore_robot" : { "ore" : 2 }, 
    "clay_robot" : { "ore" : 3 }, 
    "obsidian_robot" : { "ore" : 3, "clay" : 8 }, 
    "geode_robot" :{ "ore" : 3, "obsidian" : 12 } 
  } 
]

def copy_state(state):
  return {
    "ore_robot" : state["ore_robot"],
    "clay_robot" : state["clay_robot"],
    "obsidian_robot" : state["obsidian_robot"],
    "geode_robot" : state["geode_robot"],
    "ore" : state["ore"],
    "clay" : state["clay"],
    "obsidian" : state["obsidian"],
    "geode" : state["geode"]
  }

def get_initial_state():
  return {
    "ore_robot" : 1,
    "clay_robot" : 0,
    "obsidian_robot" : 0,
    "geode_robot" : 0,
    "ore" : 0,
    "clay" : 0,
    "obsidian" : 0,
    "geode" : 0
  }

def biggest_bois(states, blueprint, max_count, time_remaining):
  ore_ratio = max([1,blueprint["obsidian_robot"]["ore"]/blueprint["obsidian_robot"]["clay"]])
  clay_ratio = max([1,blueprint["obsidian_robot"]["clay"]/blueprint["obsidian_robot"]["ore"]])
  def matrix_reloaded(state):
    val = 0
    val += (state["ore_robot"] * time_remaining * 5 + state["ore"]) * ore_ratio
    val += (state["clay_robot"] * time_remaining * 5 + state["clay"]) * clay_ratio
    val += (state["obsidian_robot"] * time_remaining * 5 + state["obsidian"]) * (10 + ore_ratio + clay_ratio)
    val += (state["geode_robot"] * time_remaining * 5 + state["geode"]) * (100 + ore_ratio + clay_ratio)
    return val
    
  return sorted(states, reverse=True, key=matrix_reloaded)[0:max_count]

def can_purchase(blueprint, state, robot_name):
  costs = blueprint[robot_name]
  retval = True
  for cost in costs:
    retval = retval and (costs[cost] <= state[cost])
  return retval

def advance_state(blueprint, states, time_remaining, max_count=40000):
  new_states=[]
  robot_names = [i for i in blueprint.keys() if "_robot" in i]
  for state in states:
    #decide purchases
    purchase_options = [i for i in robot_names if can_purchase(blueprint, state, i)]

    #update ore counts
    for robot_name in robot_names:
      ore_name = robot_name.split('_')[0]
      state[ore_name] += state[robot_name]

    #accrue purchases
    new_states.append(copy_state(state))
    for robot_name in purchase_options:
      new_state = copy_state(state)
      new_state[robot_name] += 1
      for cost in blueprint[robot_name]:
         new_state[cost] -= blueprint[robot_name][cost]
      new_states.append(new_state)
  return biggest_bois(new_states, blueprint, max_count, time_remaining)
    

def get_max_geodes(blueprint, minute_count = 24):
  states = [get_initial_state()]
  while minute_count > 0:
    print(minute_count)
    states = advance_state(blueprint, states, minute_count)
    minute_count -= 1

  
  x = max([i["geode"] for i in states])
  tests = [i for i in states if i["geode"] == x]
  #print(len(tests))
  #print(tests[0])
  return x


bests = []
for blueprint in blueprints:
  best = get_max_geodes(blueprint)
  print()
  print(" - {}".format(best))
  print()
  bests.append(best)


print()
print(bests)

x=0
for i in range(len(bests)):
  x += (i+1)*bests[i]
print(x)
# --------------------- Part 2 --------------------- #

#print(data)
