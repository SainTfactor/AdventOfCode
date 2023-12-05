#!/usr/bin/env python3
from data import data
def parse_line(line):
    games = []
    for i in line.split("; "):
        game = { "red" : 0, "green" : 0, "blue" : 0 }
        for j in i.split(", "):
            number = int(j.split(" ")[0])
            if "red" in j:
                game["red"] = number
            if "green" in j:
                game["green"] = number
            if "blue" in j:
                game["blue"] = number
        games.append(game)
    return games



def parse_data(stuff):
    x = stuff.split("\n")[1:-1]
    y = [parse_line(i.split(": ")[1]) for i in x]
    return y

def test_good(game):
    if game["red"] > 12:
        return False
    if game["green"] > 13:
        return False
    if game["blue"] > 14:
        return False
    return True

dataa = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

data = parse_data(data)

print(data)
print(len(data))

val = 0
for i in range(len(data)):
    good = True
    for j in data[i]:
        if not test_good(j):
            good = False
    if good:
        val += i + 1
print(val)

# --------------------- Part 2 --------------------- #


val = 0
for i in data:
    mins = [0,0,0]
    for j in i:
        if j["red"] > mins[0]:
            mins[0] = j["red"]
        if j["green"] > mins[1]:
            mins[1] = j["green"]
        if j["blue"] > mins[2]:
            mins[2] = j["blue"]
    val += mins[0]*mins[1]*mins[2]
print(val)

