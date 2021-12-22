#!/usr/bin/env python3
from data import data

#data = ["[({(<(())[]>[[{[]{<()<>>", "[(()[<>])]({[<{<<[]>>(", "{([(<{}[<>[]}>{[]{[(<()>", "(((({<>}<{<{<>}{[]{[]{}", "[[<[([]))<([[{}[[()]]]", "[{[{({}]{}}([{[{{{}}([]", "{<[[]]>}<{[{[{[]{()[[[]", "[<(<(<(<{}))><([]([]()", "<{([([[(<>()){}]>(<<{{", "<{([{{}}[<[[[<>{}]]]>[]]"]
#print(data)

point_tracker = { ")" : 0, "]" : 0, "}" : 0, ">" : 0 }
good_autocompletes = []

for datum in data:
    next_close = []
    error = False
    for d in datum:
        if d == '(':
            next_close.append(')')
        elif d == '[':
            next_close.append(']')
        elif d == '{':
            next_close.append('}')
        elif d == '<':
            next_close.append('>')
        else:
            good = next_close.pop()
            if d != good:
                error = True
                point_tracker[d] += 1

    if not error:
        good_autocompletes.append("".join(reversed(next_close)))

#print(point_tracker)
#print((point_tracker[')']*3)+(point_tracker[']']*57)+(point_tracker['}']*1197)+(point_tracker['>']*25137))

output = []
scorings = { ')' : 1, ']' : 2, '}' : 3, '>' : 4}
for ga in good_autocompletes:
    runner = 0
    for char in ga:
        runner = (runner * 5) + scorings[char]
    output.append(runner)
print(output)
temp = sorted(output)
print(temp[len(temp)//2])
