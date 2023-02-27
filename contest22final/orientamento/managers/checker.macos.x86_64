#!/usr/bin/env python3

#
# Checker Final Contest LUISSMatics 2022
# Task n. 2 "Orientamento"
# Maria Chiara Lischi, Matteo Spadaccia
#

import string
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
T = 50 # number of test cases

outputs = []

#!/usr/bin/env python3

def maxAf (N, P, a, x): 
    A = a
    y = (100*x)/(100+x)
    flag = False
    
    for i in range(N-1):
        b = (a*(100+x)/100)
        if b <= P:
            a = b
            A += a
        else:
            flag = True
            break
    
    if flag and (N-1-i)%2 == 0:
        A += ((N-1-i)/2)*a
        a = a*(100-y)/100
        A += ((N-1-i)/2)*a
    elif flag:
        A += (((N-1-i)-1)/2)*a
        a = a*(100-y)/100
        A += (((N-1-i)+1)/2)*a
        
    return int(A)

for caso in range(T):
    task_input.readline()
    line = task_input.readline()
    N, P, a, x = line.strip().split(" ")
    N, P, a, x = int(N), int(P), int(a), int(x)
    res = maxAf (N, P, a, x)
    outputs.append(res)

def evaluate(num, stream):
    correct_output = outputs[num-1]
    output = stream.str()
    try:
        output = int(output)
    except ValueError:
        pass
    if output == correct_output:
        return 1.0
    else:
        return 0.0

parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False)

print(json.dumps(parser.run()))