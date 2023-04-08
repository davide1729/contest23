#!/usr/bin/env python3

#####
# Final Contest LUISSTraining 2023
# Task n. 3 "PageRank"
# SOLUTION CHECKER
# Demetrio F. Cardile, Davide Beltrame
#####

from distutils.command.build_scripts import first_line_re
import networkx as nx
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
T = int(task_input.readline())
a0 = int(task_input.readline())

def pagerank():
    mypr = {}
    k_out = {}
    a = a0/10

    for i in neighbors:
        mypr[i]=1/N 
        k_out[i]=len(neighbors[i])

    iterations = 0  
    while True:
        diff = 0
        mypr2 = mypr.copy() # we create a clone of mypr in order to distinguish two contiguous iterations
        for i in mypr2:
            sum = 0
            for j in neighbors[i]:
                sum += mypr2[j]/k_out[j]        
            mypr2[i]= a/N + (1-a)*sum
        #print(mypr2[1])    
        iterations += 1 # iteration counter

        for i in mypr2:
            diff = abs(mypr[i] - mypr2[i]) # we check if *all* the values are the same
            if diff < 10**-6: # in order to check the convergence between two iterations
                a = 1 
            
        if a == 1:
            break
        
        mypr = mypr2
    global max
    max = 0
    for i in mypr:
        if i+1 >= len(mypr):
            continue
        else:
            if mypr[i+1]>mypr[i]:
                max = i+1

def pagerank2():

    G = nx.Graph()
    G.add_nodes_from(neighbors.keys())
    for node, neighbours in neighbors.items():
        for neighbour in neighbours:
            G.add_edge(node, neighbour)

    pr = nx.pagerank(G)

    global max
    max = 0
    for i in pr:
        if i+1 >= len(pr):
            continue
        else:
            if pr[i+1]>pr[i]:
                max = i+1

for t in range(T):
    task_input.readline()
    N = int(task_input.readline())
    neighbors = {}
    for node in range(0,N):
        neighbors[node] = []
        neighbors[node] = [ int(x) for x in task_input.readline().strip().split(" ") ]
        neighbors[node].remove(neighbors[node][0])
    pagerank()
    res = max
    outputs.append(str(res))

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