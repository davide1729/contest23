#!/usr/bin/env python3

# temp CHECKER SKELETON
# generated from code sections common to all checkers

#
# Checker Intermediate Contest LUISSMatics 2022
# Task n. 4 "Droni spia (spia)"
# Michele Lizzit, Davide Beltrame
#

from sortedcontainers import SortedSet
from itertools import accumulate
from parser import Parser
from sys import argv, exit, stderr
import json

if len(argv) != 3:
    print("Usage: %s input_file output_file" % argv[0], file=stderr)
    exit(1)

task_input = open(argv[1], "r")
human_output = open(argv[2], "r")

# reading input file and generating correct output
T = int(task_input.readline())

outputs = []



#!/usr/bin/env python3

# 2
#
# 2
# 7 7 6 5 1 2 8 9
# 3 3 1 1
#
# 1
# 3 20 2 5

cnt = 0

def destroy(i, todo):
    if i not in todo:
        return True

    global cnt
    tt = i[0]
    i = i[1]
    
    if i*2+2 <= N:
        a = (l[2*i+1], 2*i+1)
        b = (l[2*i+2], 2*i+2)

        if not (destroy(a, todo) and destroy(b, todo)):
            return False

    cnt += 2
    todo.remove((tt, i))
    if cnt <= tt:
        return True
    else:
        return False


for t in range(T):
    task_input.readline().strip()
    C = int(task_input.readline().strip())
    out = []
    for c in range(C):
        cnt = 0
        l = [ int(x) for x in task_input.readline().strip().strip().split(" ") ]
        N = l[0]
        l = l[1:]
        l2 = [ (l[i],i) for i in range(len(l)) ]
        todo = SortedSet(l2)
        done = True
        while len(todo) > 0:
            v = todo.pop(index=0)
            todo.add(v)
            if not destroy(v, todo):
                done = False
                break
        if done:
            out.append("Droni_disattivati")
        else:
            out.append("Luiss_LOFT")
    outputs.append(out)



def evaluate(num, stream):
    correct_output = outputs[num-1]
    output = [ stream.str() for _ in range(len(outputs[num-1])) ]

    if output == correct_output:
        return 1.0
    else:
        return 0.0


parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False, str_max_len=10**7)

print(json.dumps(parser.run()))