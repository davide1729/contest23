#!/usr/bin/env python3

#
# Checker Gara Luiss 2021
# Task n.2 "Meme"
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
    ln=task_input.readline().split()
    N=int(ln[0])
    m=int(ln[1])
    
    w=[0]
    p=[0]
    
    for i in range(N):
        ln=task_input.readline().split()
        w.append(int(ln[0]))
        p.append(int(ln[1]))
    
    M = [ [ (0,-1) for i in range(m+1) ] for j in range(N+1) ]
    
    for i in range(1,N+1):
        for j in range(m+1):
            if(w[i]>j):
                M[i][j]=M[i-1][j]
            else:
                if(p[i]+M[i-1][j-w[i]][0]>M[i-1][j][0]):
                    M[i][j]=(p[i]+M[i-1][j-w[i]][0], i)
                else:
                    M[i][j]=M[i-1][j]
    g=N
    h=m
    ris=[]
    while(M[g][h][1]!=-1):
        meme=M[g][h][1]
        ris.append(meme)
        h-=w[meme]
        g=meme-1
    ris.reverse()
    ris.sort()

    outputs.append(ris)

def evaluate(num, stream):
    correct_output = outputs[num-1]
    output = []
    while stream.has_int():
        output.append(stream.int())
    stream.end()

    if output == correct_output:
        return 1.0
    else:
        return 0.0


parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False)

print(json.dumps(parser.run()))
