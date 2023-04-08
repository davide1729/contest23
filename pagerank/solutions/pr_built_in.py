#!/usr/bin/env python3

# soluzione pagerank built-in
# Demetrio e Davide

import networkx as nx #this is for network

T = int(input())
a0 = int(input())

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
    input()
    N = int(input())
    neighbors = {}
    for node in range(0,N):
        neighbors[node] = []
        neighbors[node] = [ int(x) for x in input().strip().split(" ") ]
        neighbors[node].remove(neighbors[node][0])
    pagerank2()
    print(f"Case #{t+1}: {max}")