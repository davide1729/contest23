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

def dfs(u, c):
    colore[u] = c
    for v in adj[u]:
        if(colore[u]==colore[v] ):
            return False
        elif (colore[v] == -1) and (not dfs(v,1-c) ):
            return False
    return True

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
    N, M = [int(x) for x in task_input.readline().split(" ")]
    mat = [[0 for x in range(N)] for _ in range(N)]    
    colore = [-1 for x in range(N)]
    adj = [[] for x in range(N)]
    n, m = N, M

    for i in range(M):
        a, b = [int(x) for x in task_input.readline().split(" ")]
        mat[a][b] = 1
        mat[b][a] = 1

    for i in range(N):
        for j in range(N):
            if i!=j and (not mat[i][j]):
                adj[i].append(j)

    ok = True

    for i in range(n):
        if colore[i] == -1:
            if not dfs(i,0):
                ok = False

    if not ok:
        res = -1
    else:
        res = adj.copy()

    outputs.append(res)

def isValidSol(g1, g2, adj):
    if len(g1) + len(g2) != len(adj):
        return False

    if len(g1) == 0:
        return False
    if len(g2) == 0:
        return False

    # If same element in both g1 and g2
    if len(set(g1).intersection(g2)) > 0:
        return False

    for e in g1:
        if len(set(adj[e]).intersection(g1)) > 0:
            return False
    for e in g2:
        if len(set(adj[e]).intersection(g2)) > 0:
            return False
    return True
            

def evaluate(num, stream):
    correct_output = outputs[num-1]
    output = stream.int()
    if output == -1 and correct_output == -1:
        stream.end()
        return 1.0
    if output == -1 or correct_output == -1:
        stream.end()
        return 0.0

    n1 = output
    g1 = [stream.int() for x in range(n1)]
    n2 = stream.int()
    g2 = [stream.int() for x in range(n2)]
    
    stream.end()

    adj = correct_output
    valid = isValidSol(g1, g2, adj)
    
    if valid:
        return 1.0
    else:
        return 0.0


parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False)

print(json.dumps(parser.run()))
