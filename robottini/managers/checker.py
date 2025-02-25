#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 4 "Robottini Mercenari"
# SOLUTION CHECKER
# Davide Beltrame
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

def get_divisors(n):
    div = []
    for ii in range(2, int(n/2) + 1):
        if n % ii == 0:
            div.append(ii)
    div.append(n)
    return div

# PREPARATION BASING ON N ONLY

def prepare_connections(N):
    # creating dictionary "divisors_dict" containing for each integer up to N a list of its divisors
    divisors_dict = {}
    for ii in range(2, N+1):
        divisors_dict[ii] = get_divisors(ii)
    
    # creating dictionary "connections_dict" containing for each integer up to N a list of its divisors and their multiples
    connections_dict = divisors_dict.copy()
    for ii in range(2, N+1):
        for jj in divisors_dict[ii]:
            for kk in range(2,N+1):
                if (jj in divisors_dict[kk]) and (kk not in connections_dict[ii]):
                    connections_dict[ii] = connections_dict[ii]+[kk]
    
    return(connections_dict)

def prepare_connections2(N, connections_dict):
    # creating dictionary "connections_dict2" containing for each integer up to N the list of numbers less than N that are not its divisors nor their multiples
    connections_dict2 = {}
    int_set = set(range(2, N+1))
    for ii in range(2, N+1):
        connections_dict2[ii] = list(int_set - set(connections_dict[ii]))
    return(connections_dict2)

def solution(inputs_dict, connections_dict2):
    inputs = inputs_dict.copy()
    # takes from the keys of the old dictionary the nodes that actually exist
    temp = {}
    for ii in inputs.keys():
        temp[ii] = connections_dict2[ii]
    
    # creating dictionary "acutal_connections_dict2" containing for each integer of input the other integers that choosing it would not cut
    actual_connections_dict2 = {} 
    for ii in inputs.keys():
        actual_connections_dict2[ii] = []
        for jj in temp[ii]:
            if jj in inputs.keys():
                actual_connections_dict2[ii] = actual_connections_dict2[ii]+[jj]  
    
    G = nx.Graph()
    for ii in inputs.keys():
        G.add_node(ii)
    
    for ii in inputs.keys():
        for jj in actual_connections_dict2[ii]:
            if (ii, jj) not in G.edges():
                G.add_edge(ii, jj)
    
    conn_comp = sorted(nx.find_cliques(G), key=len, reverse=True)
    global max_val
    max_val = 0
    for selected in conn_comp:
        val = 0
        for ii in selected:
            val += inputs[ii]
        if max_val < val:
            max_val = val
            solution = selected
    
    return(solution, max_val)

T = int(task_input.readline())

for t in range(T):
    task_input.readline()
    N = int(task_input.readline())
    M = int(task_input.readline())
    models = {}
    models_list = [ int(x) for x in task_input.readline().strip().split(" ") ]
    power_list = [ int(x) for x in task_input.readline().strip().split(" ") ]
    for n in range(N):
        models[models_list[n]] = power_list[n]
    connections = prepare_connections(M)
    connections_2 = prepare_connections2(M, connections)
    solution(models, connections_2)
    res = max_val

    outputs.append(str(res))

def evaluate(num, stream):
    correct_output = int(outputs[num-1]) # quelli del checker
    user_output = int(stream.str()) # quello della soluzione
    stream.end()
    if correct_output - user_output >= 0 and (correct_output - user_output)/correct_output < 0.05:
        return 1.0
    else:
        return 0.0

parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False)

print(json.dumps(parser.run()))