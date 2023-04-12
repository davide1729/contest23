#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 4 "Robottini Mercenari"
# BRUTEFORCE SOLUTION
# Maria Chiara Lischi, Matteo Spadaccia
#####

import itertools

def get_divisors(n):
    div = []
    for ii in range(2, int(n/2) + 1):
        if n % ii == 0:
            div.append(ii)
    div.append(n)
    return div

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

def empirical(inputs_dict, connections_dict):
    
    int_list = list(inputs_dict.keys())
    n = len(int_list)

    int_combinations = list()
    for selected_n in range(n+1):
        int_combinations += list(itertools.combinations(int_list, selected_n))

    possible_combinations = {}
    for combination in int_combinations:
        violation = False
        for ii in combination:
            for jj in combination:
                if ii != jj and jj in connections_dict[ii]:
                    violation = True
                    break
            if violation:
                break
    
        if not violation:
            possible_combinations[combination] = 0
            for ii in combination:
                possible_combinations[combination] += inputs_dict[ii]

    max_value_combination = max(possible_combinations, key=possible_combinations.get)
    return(list(max_value_combination), possible_combinations[max_value_combination])

T = int(input()) # numero di casi di test

for t in range(T):
    input() # spazio
    N = int(input())
    M = int(input())
    models = {}
    models_list = [ int(x) for x in input().strip().split(" ") ]
    power_list = [ int(x) for x in input().strip().split(" ") ]
    for n in range(N):
        models[models_list[n]] = power_list[n]
    connections = prepare_connections(M)
    res = empirical(models,connections)
    # adattare la risoluzione per inserirla in "res"
    print(f"Case #{t+1}: {res}") # output bruteforce