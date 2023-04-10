import itertools
import networkx as nx

def get_divisors(n):
    div = []
    for ii in range(2, int(n/2) + 1):
        if n % ii == 0:
            div.append(ii)
    div.append(n)
    return div

# PREPARATION BASING ON N ONLY

def prepare_connections(N):
    # creating dictionary "divisors_dict" containing for each integer up to N a list of its divisors
    divisors_dict = {}
    for ii in range(2, N+1):
        divisors_dict[ii] = get_divisors(ii)
    
    # creating dictionary "connections_dict" containing for each integer up to N a list of its divisors and their multiples
    connections_dict = divisors_dict.copy()
    for ii in range(2, N+1):
        for jj in divisors_dict[ii]:
            for kk in range(2,N+1):
                if (jj in divisors_dict[kk]) and (kk not in connections_dict[ii]):
                    connections_dict[ii] = connections_dict[ii]+[kk]
    
    return(connections_dict)

def prepare_connections2(N, connections_dict):
    # creating dictionary "connections_dict2" containing for each integer up to N the list of numbers less than N that are not its divisors nor their multiples
    connections_dict2 = {}
    int_set = set(range(2, N+1))
    for ii in range(2, N+1):
        connections_dict2[ii] = list(int_set - set(connections_dict[ii]))
    return(connections_dict2)

def solution(inputs_dict, connections_dict2):
    inputs = inputs_dict.copy()
    # takes from the keys of the old dictionary the nodes that actually exist
    temp = {}
    for ii in inputs.keys():
        temp[ii] = connections_dict2[ii]
    
    # creating dictionary "acutal_connections_dict2" containing for each integer of input the other integers that choosing it would not cut
    actual_connections_dict2 = {} 
    for ii in inputs.keys():
        actual_connections_dict2[ii] = []
        for jj in temp[ii]:
            if jj in inputs.keys():
                actual_connections_dict2[ii] = actual_connections_dict2[ii]+[jj]  
    
    G = nx.Graph()
    for ii in inputs.keys():
        G.add_node(ii)
    
    for ii in inputs.keys():
        for jj in actual_connections_dict2[ii]:
            if (ii, jj) not in G.edges():
                G.add_edge(ii, jj)
    
    conn_comp = sorted(nx.find_cliques(G), key=len, reverse=True)
    
    max_val = 0
    for selected in conn_comp:
        val = 0
        for ii in selected:
            val += inputs[ii]
        if max_val < val:
            max_val = val
            solution = selected
    
    return(solution, max_val)