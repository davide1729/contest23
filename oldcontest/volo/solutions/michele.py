#!/usr/bin/env python3

"""
@author: Michele Lizzit
(adapted from carlo.py)

Task: VoloAngelo
"""

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

T=int(input())

for t in range(1,T+1):
    input()
    ln=input().split()
    N=int(ln[0])
    D=int(ln[1])
    
    X=[]
    Y=[]
    H=[]
    adj=[[] for i in range(N)]
    
    H_max=0
    H_idx=0
    
    for i in range(N):
        ln=input().split()
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

    print("Case #{}:".format(t), int(round(findlongestpath(adj, H_idx),0)))
