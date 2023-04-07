#!/usr/bin/env python3

# soluzione pagerank
# Demetrio e Davide

import networkx as nx #this is for network
import time # this is to get computational time

T = int(input())
a0 = int(input())

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

for t in range(T):
    input()
    N = int(input())
    neighbors = {}
    for node in range(0,N):
        neighbors[node] = []
        neighbors[node] = [ int(x) for x in input().strip().split(" ") ]
        neighbors[node].remove(neighbors[node][0])
    pagerank()
    print(f"Case #{t+1}: {max}")



