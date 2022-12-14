#!/usr/bin/env python3
from data import order, boards

#order = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
#boards = [[22, 13, 17, 11, 0],[8, 2, 23, 4, 24],[21, 9, 14, 16, 7],[6, 10, 3, 18, 5],[1, 12, 20, 15, 19]],[[3, 15, 0, 2, 22],[9, 18, 13, 17, 5],[19, 8, 7, 25, 23],[20, 11, 10, 24, 4],[14, 21, 16, 12, 6]],[[14, 21, 17, 24, 4],[10, 16, 15, 9, 19],[18, 8, 23, 26, 20],[22, 11, 13, 6, 5],[2, 0, 12, 3, 7]]

def check_board(calls, board):
    ret_val = False
    for i in range(5):
        #check h
        if len([j for j in board[i] if j in calls]) == 5:
            ret_val = True
            break
        #check v
        if len([j[i] for j in board if j[i] in calls]) == 5:
            ret_val = True
            break
    #check d
    if [board[4-i][i] for i in range(5) if board[4-i][i] in calls] == 5 or [board[i][i] for i in range(5) if board[i][i] in calls] == 5:
        ret_val = True
    return ret_val

solution = None
on_call = -1
i_on_call = -1
for i in range(len(order)):
    for b in boards:
        done = check_board(order[0:i], b)
        if done:
            solution = b
            on_call = order[i-1]
            i_on_call = i
            break
    if on_call != -1:
        break

score=sum([sum([j for j in i if not j in order[0:i_on_call]]) for i in solution])
print(score)
print(on_call)
print(on_call*score)

print('-'*100)

solution = None
on_call = -1
i_on_call = -1
for i in range(len(order)):
    done = False
    kill_me = []
    for b in range(len(boards)):
        done = check_board(order[0:i], boards[b])
        if done:
            kill_me.append(b)
    for b in kill_me:
        if len(boards) == 1:
            solution = boards[0]
        boards = boards[0:b] + boards[b+1:]
    if len(boards) == 0:
        on_call = order[i-1]
        i_on_call = i
        break

score=sum([sum([j for j in i if not j in order[0:i_on_call]]) for i in solution])
print(score)
print(on_call)
print(on_call*score)
