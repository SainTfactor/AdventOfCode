#!/usr/bin/env python3
from data import data

#data = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0], [3, 9, 8, 7, 8, 9, 4, 9, 2, 1], [9, 8, 5, 6, 7, 8, 9, 8, 9, 2], [8, 7, 6, 7, 8, 9, 6, 7, 8, 9], [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]
#print(data)

lows = []
for x in range(len(data)):
    for y in range(len(data[0])):
        my_point = data[x][y]
        try:
            if data[x+1][y] <= my_point:
                continue
        except:
            pass

        try:
            assert (x-1)>=0
            if data[x-1][y] <= my_point:
                continue
        except:
            pass

        try:
            if data[x][y+1] <= my_point:
                continue
        except:
            pass

        try:
            assert (y-1)>=0
            if data[x][y-1] <= my_point:
                continue
        except:
            pass

        lows.append((x,y))

#print(lows)
#print([data[i[0]][i[1]] for i in lows])
#print([data[i[0]][i[1]] + 1 for i in lows])
print(sum([data[i[0]][i[1]] + 1 for i in lows]))


def calc_basin(low, runner=[]):
    if low in runner:
        return 0
    runner.append(low)
    x = low[0]
    y = low[1]
    my_point = data[x][y]
    ret_val = 1
    try:
        assert data[x+1][y] != 9
        if data[x+1][y] >= my_point:
            ret_val += calc_basin((x+1,y))
    except:
        pass

    try:
        assert (x-1)>=0
        assert data[x-1][y] != 9
        if data[x-1][y] >= my_point:
            ret_val += calc_basin((x-1,y))
    except:
        pass

    try:
        assert data[x][y+1] != 9
        if data[x][y+1] >= my_point:
            ret_val += calc_basin((x,y+1))
    except:
        pass

    try:
        assert (y-1)>=0
        assert data[x][y-1] != 9
        if data[x][y-1] >= my_point:
            ret_val += calc_basin((x,y-1))
    except:
        pass

    return ret_val


basins=[]
for low in lows:
    basins.append(calc_basin(low))
final = sorted(basins, reverse=True)
print(final)
print(final[0]*final[1]*final[2])
