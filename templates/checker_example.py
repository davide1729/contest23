#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. x "Nome Task"
# SOLUTION CHECKER
# Autori
#####

from distutils.command.build_scripts import first_line_re
# import librerie necessarie
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

# funzioni per risolvere il problema

T = int(task_input.readline())

for t in range(T):
    res = "la soluzione che viene dopo Case #x: "
    task_input.readline()
	# mettere soluzione in res
    outputs.append(res)

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