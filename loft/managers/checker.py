#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 4 "Breaking into LOFT"
# SOLUTION CHECKER
# Francesca Romana Sanna, Leonardo Azzi
#####

from distutils.command.build_scripts import first_line_re
from functools import lru_cache
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

outputs = [] 

def decoder(test):
    global result
    matrix = {}
    cursor_index = [0, 0]
    for i in test:
        if i == '{' or i == '}':
            continue
        elif i == '_':
            cursor_index[0] = cursor_index[0] + 1
            matrix[cursor_index[0]] = matrix.get(cursor_index[0], [])
            cursor_index[1] = min(len(matrix[cursor_index[0]]), cursor_index[1])
            #Se necessario, implementare un cap massimo di "profondità" (usa min(max_depth, cursor_index[0] + 1))
        elif i == '^':
            cursor_index[0] = max(0, cursor_index[0] - 1)
            matrix[cursor_index[0]] = matrix.get(cursor_index[0], [])
            cursor_index[1] = min(len(matrix[cursor_index[0]]), cursor_index[1])
        elif i == '>':
            cursor_index[1] = min(len(matrix[cursor_index[0]]), cursor_index[1] + 1)
        elif i == '<':
            cursor_index[1] = max(0, cursor_index[1] - 1)
            #print(f"Cursor index: {cursor_index[1]}")
        elif i.isdigit():
            matrix[cursor_index[0]] = matrix.get(cursor_index[0], [])
            matrix[cursor_index[0]].insert(cursor_index[1], int(i))
            cursor_index[1] += 1
            #print(matrix)
    result = []
    for n in range(len(matrix)):
        result.append(matrix[n])

T = int(task_input.readline())

for t in range(T):
    task_input.readline()
    decoder()
	# mettere soluzione in res
    outputs.append(str(result))

def evaluate(num, stream):
    correct_output = outputs[num-1] # quelli del checker
    user_output = stream.str() # quello della soluzione
    stream.end()
    if user_output == correct_output:
        return 1.0
    else:
        return 0.0

parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False)

print(json.dumps(parser.run()))