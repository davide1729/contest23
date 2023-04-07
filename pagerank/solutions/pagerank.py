#!/usr/bin/env python3

# soluzione pagerank
# Demetrio e Davide

import random #random generator
import networkx as nx #this is for network
import matplotlib.pyplot as plt #this is for drawing
import numpy as np #this is for matrices
import csv #this is to read csv files
import time # this is to get computational time
import pandas as pd # this is for dataframes
import math # some math tools for week 5

'''neighbors = {0:[1,3,4],
             1:[0,2,3,4],
             2:[1,4],
             3:[0,1,4],
             4:[0,1,2,3]
             }'''

def pagerank():
    mypr = {}
    k_out = {}
    #N = number_of_nodes    

    for i in neighbors:
        mypr[i]=1/N 
        k_out[i]=len(neighbors[i])

    iterations = 0  
    a = 0.15
    while True:
        diff = 0
        mypr2 = mypr.copy() # we create a clone of mypr in order to distinguish two contiguous iterations
        for i in mypr2:
            sum = 0
            for j in neighbors[i]:
                sum += mypr2[j]/k_out[j]        
            mypr2[i]= a/N + (1-a)*sum
        print(mypr2[1])    
        iterations += 1 # iteration counter

        for i in mypr2:
            diff = abs(mypr[i] - mypr2[i]) # we check if *all* the values are the same
            if diff < 10**-6: # in order to check the convergence between two iterations
                a = 1 
            
        if a == 1:
            break
        
        mypr = mypr2

    max = 0
    for i in mypr:
        if i+1 >= len(mypr):
            continue
        else:
            if mypr[i+1]>mypr[i]:
                max = i+1

T = int(input())
a0 = int(input())
a = a0/10

for t in range(T):
    input()
    N = int(input())
    neighbors = {}
    for node in range(0,N):
        print(node)
        neighbors[node] = []
        keys = [ int(x) for x in input().strip().split(" ") ]
        print(keys)
        





#######################


# PageRank scores computation
#pr = nx.pagerank(G)   # returns a dictionary

# Separately save the values of the dictionary
#pr_values = pr.values()