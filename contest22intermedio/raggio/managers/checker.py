#!/usr/bin/env python3

#
# Checker Intermediate Contest LUISSMatics 2022
# Task n. 3 "Raggio Hackerante (raggio)"
# Michele Lizzit
#

from itertools import accumulate
from parser import Parser
import json
from sys import argv, exit, stderr

if len(argv) != 3:
    print("Usage: %s input_file output_file" % argv[0], file=stderr)
    exit(1)

task_input = open(argv[1], "r")
human_output = open(argv[2], "r")

# reading input file and generating correct output
T = int(task_input.readline().strip())

outputs = []

for t in range(T):
    task_input.readline().strip()
    N, P = task_input.readline().strip().strip().split(" ")
    N, P = int(N), int(P)
    l = [int(x) for x in task_input.readline().strip().strip().split(" ")]

    cur = l[0]
    i, j = 0, 0
    end = False
    best = i, j, cur
    while not end:
        if cur < P and j < N - 1:
            j += 1
            cur += l[j]
        elif cur > P and i < j:
            cur -= l[i]
            i += 1
        elif cur > P and i == j and j < N - 1:
            j += 1
            cur += l[j]
            cur -= l[i]
            i += 1
        else:
            end = True
        if abs(cur - P) < abs(best[2] - P):
            best = i, j, abs(cur)
    outputs.append((best[2], l))

def evaluate(num, stream):
    correct_output, l = outputs[num-1][0], outputs[num-1][1]
    i,j = sorted([ stream.int(), stream.int() ])
    user_output = sum(l[i:j + 1])
    stream.end()
    if correct_output == user_output:
        return 1.0
    else:
        return 0.0

parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False)

print(json.dumps(parser.run()))