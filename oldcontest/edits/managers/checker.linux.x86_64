#!/usr/bin/env python3

#
# Checker Gara Luiss 2021
# Task n.1 "Quiz"
# Michele Lizzit
#

from itertools import accumulate
from parser import Parser
from sys import argv, exit, stderr
import json
from blist import blist

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
    inp = task_input.readline().strip().replace("[L]", "<").replace("[R]", ">").replace("[C]", "!")
    res = blist()
    poi = 0
    for e in inp:
        if poi == 0 and (e == "<" or e == "!"):
            continue
        if len(res) == poi and e == ">":
            continue
        if e == "<":
            poi -= 1
            continue
        if e == ">":
            poi += 1
            continue
        if e == "!":
            poi -= 1
            del res[poi]
            continue
        res.insert(poi, e)
        poi += 1
    res = "".join(res)

    outputs.append(res)

def evaluate(num, stream):
    correct_output = outputs[num-1]
    output = stream.str()
    stream.end()

    if output == correct_output:
        return 1.0
    else:
        return 0.0


parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False, str_max_len=10**7)

print(json.dumps(parser.run()))
