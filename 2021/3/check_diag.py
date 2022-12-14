#!/usr/bin/env python3
from diagnostics import diagnostics

#diagnostics = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
#print(diagnostics)

gamma = ""
epsilon = ""
half = len(diagnostics)/2
for i in range(len(diagnostics[0])):
    ones = len([j for j in diagnostics if j[i] == '1'])
    if ones > half:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print("{} => {}".format(gamma, int(gamma, 2)))
print("{} => {}".format(epsilon, int(epsilon, 2)))
print(int(gamma, 2)*int(epsilon, 2))

print("-"*100)

o2 = ""
co2 = ""
ro2 = diagnostics
rco2 = diagnostics
for i in range(len(diagnostics[0])):
    if len(ro2) != 1:
        o2h = len(ro2)/2
        o21s = len([j for j in ro2 if j[i] == '1'])
        if o21s >= o2h:
            ro2 = [j for j in ro2 if j[i] == '1']
        else:
            ro2 = [j for j in ro2 if j[i] == '0']

    if len(rco2) != 1:
        co2h = len(rco2)/2
        co21s = len([j for j in rco2 if j[i] == '1'])
        if co21s >= co2h:
            rco2 = [j for j in rco2 if j[i] == '0']
        else:
            rco2 = [j for j in rco2 if j[i] == '1']


o2=ro2[0]
co2=rco2[0]

print("{} => {}".format(o2, int(o2, 2)))
print("{} => {}".format(co2, int(co2, 2)))
print(int(o2, 2)*int(co2, 2))
