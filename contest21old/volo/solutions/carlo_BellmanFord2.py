#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:09:46 2021

@author: Carlo
"""
import math

from collections import deque

def BellmanFord(N,adj, src): 
    
    dist=[2147483648 for i in range(N)]
    inq=[False for i in range(N)]
    inq[src] = True
    q = deque()
    q.append(src); dist[src] = 0;
    while(q):
        t = q.popleft()
        inq[t] = False
        for e in adj[t]:
            tn=e[0]
            if(dist[tn]>dist[t]+e[1]):
                dist[tn]=dist[t]+e[1]
                if (not(inq[tn])):
                    inq[tn]=True
                    q.append(tn)
            
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
        for j in range(i):
            dis=distance(X[i], Y[i], X[j], Y[j])
            if dis<D:
                if(H[i]>H[j]):
                    adj[i].append((j, -dis))
                elif(H[j]>H[i]):
                    adj[j].append((i, -dis))
    print("Case #{}:".format(t), int(round(BellmanFord(N, adj, H_idx),0)))
    
