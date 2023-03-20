#!/usr/bin/env python3

import math
def BellmanFord(N,edges, src): 
  
    dist = [float("Inf")] * N
    dist[src] = 0
  
    for _ in range(N - 1): 
        for u, v, w in edges: 
            if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                dist[v] = dist[u] + w 
    return -min(dist[z] for z in range(N))
    
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
    edges=[]
    
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
        for j in range(i):
            dis=distance(X[i], Y[i], X[j], Y[j])
            if dis<=D:
                if(H[i]>H[j]):
                    edges.append((i, j, -dis))
                elif(H[j]>H[i]):
                    edges.append((j, i, -dis))
    
    print("Case #{}:".format(t), int(round(BellmanFord(N,edges, H_idx),0)))
