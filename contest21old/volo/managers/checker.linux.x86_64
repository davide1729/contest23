#!/usr/bin/env python3

#
# Checker Gara Luiss 2021
# Task n.5 "Volo"
# Michele Lizzit
#

from itertools import accumulate
from parser import Parser
from sys import argv, exit, stderr
import json

from scipy.spatial import ckdtree
import math

def indegreesCalc(graph):
	indegrees = {}
	for i in range(len(graph)):
		indegrees[i] = 0
	for u in range(len(graph)):
		for v in graph[u]:
			indegrees[v[0]] += 1
	return indegrees


def toposort(graphunsorted):
	indegrees = indegreesCalc(graphunsorted)
	graphsorted = []
	stack = []

	for i in range(len(indegrees)):
		if indegrees[i] == 0:
			stack.append(i)

	while stack:
		node = stack.pop()
		graphsorted.append(node)
		#print(node, indegrees)

		if len(graphunsorted[node]) == 0:
			continue
		else:
			for n in graphunsorted[node]:
				indegrees[n[0]] -= 1
				if indegrees[n[0]] == 0:
					stack.append(n[0])
	#print(graphsorted)
	return graphsorted

def findlongestpath(graph, idx):
	graphsorted = toposort(graph)
	dist = {}
	for i in range(len(graphsorted)):
		dist[i] = -2147483648
	dist[idx] = 0

	for u in graphsorted:
		for v in graph[u]:
			if dist[int(v[0])] < ((dist[u]) + v[1]):
				dist[int(v[0])] = ((dist[u]) + v[1])
	return max(dist[i] for i in range(len(graphsorted)))

def distance(xa,ya,xb,yb):
    return math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))


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
    D=int(ln[1])
    
    X=[]
    Y=[]
    H=[]
    adj=[[] for i in range(N)]
    
    H_max=0
    H_idx=0
    
    for i in range(N):
        ln=task_input.readline().split()
        X.append(int(ln[0]))
        Y.append(int(ln[1]))
        H.append(int(ln[2]))
        if H[i]>H_max:
            H_max=H[i]
            H_idx=i

    nodes = [ (x,y) for x,y in zip(X, Y) ]

    tree = ckdtree.cKDTree(nodes)
    pairs = tree.query_pairs(D)

    for i,j in pairs:
        dis=distance(X[i], Y[i], X[j], Y[j])
        if dis<=D:
            if(H[i]>H[j]):
                adj[i].append((j, dis))
            elif(H[j]>H[i]):
                adj[j].append((i, dis))

    res = int(round(findlongestpath(adj, H_idx),0))
    outputs.append(res)

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
