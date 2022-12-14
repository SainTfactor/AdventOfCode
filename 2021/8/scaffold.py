#!/usr/bin/env python3
from data import data

#data = [(["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"], ["fdgacbe", "cefdb", "cefbgd", "gcbe"]),(["edbfga", "begcd", "cbg", "gc", "gcadebf", "fbgde", "acbgfd", "abcde", "gfcbed", "gfec"], ["fcgedb", "cgb", "dgebacf", "gc"]),(["fgaebd", "cg", "bdaec", "gdafb", "agbcfd", "gdcbef", "bgcad", "gfac", "gcb", "cdgabef"], ["cg", "cg", "fdcagb", "cbg"]),(["fbegcd", "cbd", "adcefb", "dageb", "afcb", "bc", "aefdc", "ecdab", "fgdeca", "fcdbega"], ["efabcd", "cedba", "gadfec", "cb"]),(["aecbfdg", "fbg", "gf", "bafeg", "dbefa", "fcge", "gcbea", "fcaegb", "dgceab", "fcbdga"], ["gecf", "egdcabf", "bgf", "bfgea"]),(["fgeab", "ca", "afcebg", "bdacfeg", "cfaedg", "gcfdb", "baec", "bfadeg", "bafgc", "acf"], ["gebdcfa", "ecba", "ca", "fadegcb"]),(["dbcfg", "fgd", "bdegcaf", "fgec", "aegbdf", "ecdfab", "fbedc", "dacgb", "gdcebf", "gf"], ["cefg", "dcbef", "fcge", "gbcadfe"]),(["bdfegc", "cbegaf", "gecbf", "dfcage", "bdacg", "ed", "bedf", "ced", "adcbefg", "gebcd"], ["ed", "bcgafe", "cdgba", "cbgef"]),(["egadfb", "cdbfeg", "cegd", "fecab", "cgb", "gbdefca", "cg", "fgcdab", "egfdb", "bfceg"], ["gbdfcae", "bgc", "cg", "cgb"]),(["gcafb", "gcf", "dcaebfg", "ecagb", "gf", "abcdeg", "gaef", "cafbge", "fdbac", "fegbdc"], ["fgae", "cfgab", "fg", "bagce"])]
#print(data)

def get_scaffold(all_nums):
    ones = [i for i in all_nums if len(i) == 2][0]
    sevens = [i for i in all_nums if len(i) == 3][0]
    scaffold = {}
    scaffold["".join(sorted([i for i in all_nums if len(i) == 2][0]))] = '1'
    scaffold["".join(sorted([i for i in all_nums if len(i) == 3][0]))] = '7'
    scaffold["".join(sorted([i for i in all_nums if len(i) == 4][0]))] = '4'
    scaffold["".join(sorted([i for i in all_nums if len(i) == 7][0]))] = '8'
    #3 - 5 # contains both 1's
    threes = [i for i in all_nums if len(i) == 5 and ones[0] in i and ones[1] in i][0]
    scaffold["".join(sorted([i for i in all_nums if len(i) == 5 and ones[0] in i and ones[1] in i][0]))] = '3'
    #6 - 6 # doesn't contain both 1's
    sixes = [i for i in all_nums if len(i) == 6 and not (ones[0] in i and ones[1] in i)][0]
    scaffold["".join(sorted([i for i in all_nums if len(i) == 6 and not (ones[0] in i and ones[1] in i)][0]))] = '6'
    bottom_right = [i for i in sixes if i in ones][0]
    top_right = [i for i in ones if not i in sixes][0]
    bottom_and_center = [i for i in threes if not i in sevens]
    #2 - 5 # has top right
    scaffold["".join(sorted([i for i in all_nums if len(i) == 5 and top_right in i and not bottom_right in i][0]))] = '2'
    #5 - 5 # has bottom right
    scaffold["".join(sorted([i for i in all_nums if len(i) == 5 and bottom_right in i and not top_right in i][0]))] = '5'
    #0 - 6 # doesn't have bottom and center
    scaffold["".join(sorted([i for i in all_nums if len(i) == 6 and not (bottom_and_center[0] in i and bottom_and_center[1] in i)][0]))] = '0'
    #9 - 6 # has bottom and center and top right
    scaffold["".join(sorted([i for i in all_nums if len(i) == 6 and top_right in i and bottom_and_center[0] in i and bottom_and_center[1] in i][0]))] = '9'
    return scaffold

#count = 0
#for datum in data:
#    testy = datum[1]
#    for i in testy:
#        if len(i) in [2,3,4,7]:
#            #print("{} - {}".format(len(i), i))
#            count += 1
#print(count)

runner = 0
for i in data:
    scaffold = get_scaffold(i[0])
    number = int("".join([scaffold["".join(sorted(j))] for j in i[1]]))
    runner += number
print(runner)



