#!/usr/bin/env python3

#
# Checker Gara Luiss 2021
# Task n.4 "Prolunghe"
# Michele Lizzit
#

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

for _ in range(T):
    # Solve
    task_input.readline()
    N = int(task_input.readline())
    s = [ x for x in task_input.readline() ]
    pcs = [ int(x) for x in task_input.readline().split() ]
    cor = [ pcs[i] for i in range(len(s)) if s[i] == "1" ]

    pcs.sort()
    cor.sort()

    res = 0

    if len(cor) == 1:
        for pc in pcs:
            res += abs(cor[0] - pc)
        outputs.append(res)
        continue
    
    cur_i = 0
    for pc in pcs:
        res += min( abs(pc - cor[cur_i]) , abs(cor[cur_i + 1] - pc) )
        # print(f"{ pc - cor[cur_i]} {pc} {cor[cur_i + 1] - pc }: {min( abs(pc - cor[cur_i]) , abs(cor[cur_i + 1] - pc) )}")
        if cor[cur_i + 1] == pc and cur_i + 2 < len(cor):
            cur_i += 1
    
    outputs.append(res)

def evaluate(num, stream):
    correct_output = outputs[num-1]
    output = stream.int()
    stream.end()

    if output == correct_output:
        return 1.0
    else:
        return 0.0


parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False)

print(json.dumps(parser.run()))
