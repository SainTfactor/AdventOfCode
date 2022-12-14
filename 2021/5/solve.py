#!/usr/bin/env python3
from data import data

#data = [(0,9),(5,9)], [(8,0),(0,8)], [(9,4),(3,4)], [(2,2),(2,1)], [(7,0),(7,4)], [(6,4),(2,0)], [(0,9),(2,9)], [(3,4),(1,4)], [(0,0),(8,8)], [(5,5),(8,2)]

grid = {}

def process(x,y):
    try:
        grid["{},{}".format(x,y)] += 1
    except:
        grid["{},{}".format(x,y)] = 1


def das_loop(o,t,b,d):
    for i in range(o,t+1):
        if d == 'x':
            process(i,b)
        else:
            process(b,i)

def das_loop_due(o,oo,t,tt,so=1,st=1):
    for i in range(abs(tt-t)+1):
        process(o+(i*so),t+(i*st))

for pair in data:
    a = pair[0]
    b = pair[1]
    if a[0] > b[0] and a[1] == b[1]:
        das_loop(b[0], a[0], a[1], 'x')
    elif b[0] > a[0] and a[1] == b[1]:
        das_loop(a[0], b[0], a[1], 'x')
    elif a[1] > b[1] and a[0] == b[0]:
        das_loop(b[1], a[1], a[0], 'y')
    elif b[1] > a[1] and a[0] == b[0]:
        das_loop(a[1], b[1], a[0], 'y')

    elif a[0] > b[0] and a[1] > b[1]:
        das_loop_due(a[0], b[0], a[1], b[1], -1, -1)
    elif b[0] > a[0] and a[1] > b[1]:
        das_loop_due(a[0], b[0], a[1], b[1], 1, -1)

    elif a[0] > b[0] and a[1] < b[1]:
        das_loop_due(a[0], b[0], a[1], b[1], -1)
    elif b[0] > a[0] and a[1] < b[1]:
        das_loop_due(a[0], b[0], a[1], b[1])
    
    else:
        print("sad")

#print(grid)
count = 0
for key in grid:
    if grid[key] > 1:
        count += 1
print(count)


#for x in range(10):
#    for y in range(10):
#        try:
#            print(grid["{},{}".format(y,x)], end="")
#        except:
#            print('.', end="")
#    print()
