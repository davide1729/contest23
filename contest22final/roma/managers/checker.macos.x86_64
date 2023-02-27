#!/usr/bin/env python3

from itertools import accumulate
from parser import Parser
from sys import argv, exit, stderr, setrecursionlimit
import json
import math
setrecursionlimit(15000)

if len(argv) != 3:
    print("Usage: %s input_file output_file" % argv[0], file=stderr)
    exit(1)

task_input = open(argv[1], "r")
human_output = open(argv[2], "r")

def seen(x, y, matrix):
    matrix[x][y][1] = True
    if matrix[x][y][0] == 0:
        return
    if not matrix[x - 1][y][1]:
        seen(x - 1, y, matrix)
    if not matrix[x + 1][y][1]:
        seen(x + 1, y, matrix)
    if not matrix[x - 1][y - 1][1]:
        seen(x - 1, y - 1, matrix)
    if not matrix[x - 1][y + 1][1]:
        seen(x - 1, y + 1, matrix)
    if not matrix[x + 1][y - 1][1]:
        seen(x + 1, y - 1, matrix)
    if not matrix[x + 1][y + 1][1]:
        seen(x + 1, y + 1, matrix)
    if not matrix[x][y + 1][1]:
        seen(x, y + 1, matrix)
    if not matrix[x][y - 1][1]:
        seen(x, y - 1, matrix)

# reading input file and generating correct output
T = int(task_input.readline().strip())

outputs = []
for _ in range(T):
    # Solve
    task_input.readline().strip()
    N, M = tuple(int(i) for i in task_input.readline().strip().strip().split(' '))
    
    matrix = [[[0, False]]*(M + 2)]
    for i in range(N):
        row = [[0, False]] + list([int(i), False] for i in task_input.readline().strip().strip().split(' ')) + [[0, False]]
        matrix.append(row)
    matrix.append([[0, False]]*(M + 2))
    count = 0
    for x in range(1, N + 1):
        for y in range(1, M + 1):
            if matrix[x][y][0] == 1 and (not matrix[x][y][1]):
                seen(x, y, matrix)
                count += 1
    outputs.append(count - 1)

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
