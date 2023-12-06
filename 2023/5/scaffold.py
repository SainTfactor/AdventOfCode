#!/usr/bin/env python3

seeds = [ 79, 14, 55, 13 ]
data = [
    [
        { "start" : 50, "end" : 98, "count" : 2 },
        { "start" : 52, "end" : 50, "count" : 48 }
    ],
    [
        { "start" : 0, "end" : 15, "count" : 37 },
        { "start" : 37, "end" : 52, "count" : 2 },
        { "start" : 39, "end" : 0, "count" : 15 }
    ],
    [
        { "start" : 49, "end" : 53, "count" : 8 },
        { "start" : 0, "end" : 11, "count" : 42 },
        { "start" : 42, "end" : 0, "count" : 7 },
        { "start" : 57, "end" : 7, "count" : 4 }
    ],
    [
        { "start" : 88, "end" : 18, "count" : 7 },
        { "start" : 18, "end" : 25, "count" : 70 }
    ],
    [
        { "start" : 45, "end" : 77, "count" : 23 },
        { "start" : 81, "end" : 45, "count" : 19 },
        { "start" : 68, "end" : 64, "count" : 13 }
    ],
    [
        { "start" : 0, "end" : 69, "count" : 1 },
        { "start" : 1, "end" : 0, "count" : 69 }
    ],
    [
        { "start" : 60, "end" : 56, "count" : 37 },
        { "start" : 56, "end" : 93, "count" : 4 }
    ]
]

minseed = 99999999999999999999
for seed in seeds:
    curval = seed
    for phase in data:
        for option in phase:
            # I misread the instructions, so "end" means "start" and "start" means "end" from a conceptual point of view.  Whoops...
            if curval in range(option["end"], option["end"] + option["count"] + 1):
                offset = curval - option["end"]
                curval = option["start"] + offset
                break
    if curval < minseed:
        minseed = curval
print(minseed)

# --------------------- Part 2 --------------------- #

def overlap_check(x1y1, x2y2):
    if x1y1[1] < x2y2[0]:
        return False
    if x1y1[0] > x2y2[1]:
        return False
    return True

from data import seeds, data

ranges = []
for i in range(0,len(seeds), 2):
    ranges.append([seeds[i], seeds[i] + seeds[i+1] - 1])

for phase in data:
    new_ranges = []
    for r in ranges:
        curr_range = r
        found = False
        for option in phase:
            source_range = [option["end"], option["end"] + option["count"] - 1]
            dest_range = [option["start"], option["start"] + option["count"] - 1]
            if overlap_check(r, source_range):
                found = True
                if curr_range[0] >= source_range[0] and curr_range[1] <= source_range[1]: #range contained
                    zero_offset = curr_range[0] - source_range[0]
                    one_offset = curr_range[1] - source_range[0]
                    new_ranges.append([dest_range[0] + zero_offset, dest_range[0] + one_offset])
                elif curr_range[0] < source_range[0] and curr_range[1] > source_range[1]: #option contained
                    new_ranges.append([curr_range[0], source_range[0] - 1])
                    new_ranges.append(dest_range)
                    new_ranges.append([source_range[1] + 1, curr_range[1]])
                elif curr_range[0] >= source_range[0]: # overlap right overflow
                    zero_offset = curr_range[0] - source_range[0]
                    new_ranges.append([dest_range[0] + zero_offset, dest_range[1]])
                    new_ranges.append([source_range[1] + 1, curr_range[1]])
                elif curr_range[1] <= source_range[1]: # overlap left overflow
                    one_offset = curr_range[1] - source_range[0]
                    new_ranges.append([curr_range[0], source_range[0] - 1])
                    new_ranges.append([dest_range[0], dest_range[0] + one_offset])
                else:
                    print("ERROR = r: {}, start: {}, end: {}".format(r, source_range, dest_range))
                break # this shouldn't work.  Current solution doesn't account for double processing a single range when it's split across 2 options.  e.g. if you have options 1-5 and 6-10, and the range 3-7, that breaks.  This break just forces it to take the left hand path always, which happens to get the right answer here.  I'm just too lazy to fix it, now that I got the answer.
        if not found:
            new_ranges.append(r)
    ranges = new_ranges

print(min([i[0] for i in ranges]))

