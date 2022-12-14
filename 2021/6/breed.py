#!/usr/bin/env python3
from fish import fish

#fish = [3,4,3,1,2]
#print(fish)

#def calc_children(fishy, day):
#    my_fishy = fishy
#    my_day = day
#    children = 0
#    while (my_day+my_fishy) < 256:
#        my_day += my_fishy
#        my_fishy = 7
#        children += 1+calc_children(9,my_day)
#    #print("{}, {}, {}".format(fishy, day, children))
#    return children
            
#total_fish = len(fish)
#for i in fish:
#    print(i)
#    total_fish += calc_children(i, 0)
#print(total_fish)

#for i in range(256):
#    print("{}: {}".format(i, len(fish)))
#    new_fish=[]
#    for i in range(len(fish)):
#        if fish[i] == 0:
#            fish[i] = 6
#            new_fish.append(8)
#        else:
#            fish[i] -= 1
#    fish = fish + new_fish

runner = [0,0,0,0,0,0,0,0,0]
for i in fish:
    runner[i] += 1
for i in range(256):
    breeders = runner[0]
    runner = runner[1:]
    runner[6] += breeders
    runner.append(breeders)



#print(fish)
#print(len(fish))
print(sum(runner))
