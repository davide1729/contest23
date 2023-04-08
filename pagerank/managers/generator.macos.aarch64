#!/usr/bin/env python3

#####
# Final Contest LUISSTraining 2023
# Task n. 3 "PageRank"
# INPUT GENERATOR
# Demetrio F. Cardile, Davide Beltrame
#####

import random #random generator
import networkx as nx #this is for network

# Constraints

global max_N, easy_N, average_N
max_N = 2000
easy_N = 50
average_N = 1000

# Creating the random graph using Erdős–Rényi model.

def easy_g_maker():
    global num_nodes
    num_nodes = random.randint(1,easy_N)
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

def average_g_maker():
    global num_nodes
    num_nodes = random.randint(easy_N,average_N)
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

def advanced_g_maker():
    global num_nodes
    num_nodes = random.randint(average_N,max_N)
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

def edge_case_g_maker():
    global num_nodes
    num_nodes = random.randint(average_N,max_N)
    p = 0
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

CASES = [easy_g_maker]*4 + [average_g_maker]*8 + [advanced_g_maker]*8 + [edge_case_g_maker]*5

print(len(CASES))
a = random.randint(0,9)
print(a)

for x in CASES:
    p = 0.5
    print()
    x()
    print(num_nodes)
    for node in neighbors:
        neigh = " ".join(str(x) for x in neighbors[node])
        print(node,neigh)

    

    

    