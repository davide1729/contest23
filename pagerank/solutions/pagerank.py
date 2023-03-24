import random #random generator
import networkx as nx #this is for network
import matplotlib.pyplot as plt #this is for drawing
import numpy as np #this is for matrices
import csv #this is to read csv files
import time # this is to get computational time
import pandas as pd # this is for dataframes
import math # some math tools for week 5

num_nodes = 5
p = 0.5

# Creating the random graph using Erdős–Rényi model.

neighbors = {}
G_er_standard = nx.erdos_renyi_graph(num_nodes, p)
for node in G_er_standard.nodes():
    print(node)
    for i in G_er_standard.neighbors(node):
        neighbors[node] = []
    for i in G_er_standard.neighbors(node):
        neighbors[node].append(i)
print(neighbors)
      
# Drawing the random graph
#nx.draw_networkx(G_er_standard, node_size=50, with_labels=True)
#plt.show()

print(num_nodes)
print()

'''for node in neighbors:
    neigh = str(neighbors[node])
    neigh = neigh.replace(',','')
    print(node, neigh[1:-1])'''

for node in neighbors:
    neigh = " ".join(str(x) for x in neighbors[node])
    print(node,'',neigh)


