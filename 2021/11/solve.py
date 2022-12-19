#!/usr/bin/env python3
from data import data

data = ["5483143223", "2745854711", "5264556173", "6141336146", "6357385478", "4167524645", "2176841721", "6882881134", "4846848554", "5283751526"]
data = [[int(j) for j in i] for i in data]
#print(data)

def printme():
    print(["".join([str(j) for j in i]) for i in data])

def increment():
    for one in range(len(data)):
        data[one] = [(i+1)%10 for i in data[one]]
        

printme()

increment()
printme()

increment()
printme()
