import random #random generator
import networkx as nx #this is for network
import matplotlib.pyplot as plt #this is for drawing
import numpy as np #this is for matrices
import csv #this is to read csv files
import time # this is to get computational time
import pandas as pd # this is for dataframes
import math # some math tools for week 5

# Creating the random graph using Erdős–Rényi model.

def graph_maker():
    global neighbors
    neighbors = {}
    G_er_standard = nx.erdos_renyi_graph(num_nodes, p)
    for node in G_er_standard.nodes():
        for i in G_er_standard.neighbors(node):
            neighbors[node] = []
        for i in G_er_standard.neighbors(node):
            neighbors[node].append(i)
        for i in range(0,num_nodes):  
            if i not in neighbors:  
                neighbors[i] = []
# Drawing the random graph
#nx.draw_networkx(G_er_standard, node_size=50, with_labels=True)
#plt.show()
T = 25
a = random.randint(0,9)
print(T)
print(a)
for i in range(1,T+1):
    
    num_nodes = random.randint(1,1000)
    p = 0.5
    graph_maker()
    print()
    print(num_nodes)
    

    for node in neighbors:
        neigh = " ".join(str(x) for x in neighbors[node])
        print(node,neigh)

    