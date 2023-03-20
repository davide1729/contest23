#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Sat May  8 20:10:06 2021

@author: Carlo
"""

from scipy.spatial import ckdtree
import math

graphsorted=[]
vis=[]


def dfs (adj, nodo):
    
    global graphsorted
    global vis
    
    vis[nodo]=True;
    for e in adj[nodo]:
        if(not(vis[e[0]])):
            dfs(adj, e[0]);
    graphsorted.append(nodo);


def findlongestpath(N, graph, idx):
    global vis
    global graphsorted
    
    
    vis=[False for i in range(N)]
    
    dfs(graph, idx)
    graphsorted.reverse()
    dist = {}
    for i in range(N):
        dist[i] = -2147483648
    dist[idx] = 0

    for u in graphsorted:
        for v in graph[u]:
            if dist[int(v[0])] < ((dist[u]) + v[1]):
                dist[int(v[0])] = ((dist[u]) + v[1])
    return max(dist[i] for i in range(N))

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

    pairs_index = { (x, y) : i for i,x,y in zip(range(N), X, Y) }
    nodes = [ (x,y) for x,y in zip(X, Y) ]

    tree = ckdtree.cKDTree(nodes)
    pairs = tree.query_pairs(D)

    for x,y in pairs:
        i = pairs_index[nodes[x]]
        j = pairs_index[nodes[y]]
        dis=distance(X[i], Y[i], X[j], Y[j])
        if dis<D:
            if(H[i]>H[j]):
                adj[i].append((j, dis))
            elif(H[j]>H[i]):
                adj[j].append((i, dis))

    print("Case #{}:".format(t), int(round(findlongestpath(N, adj, H_idx),0)))
