#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 4 "Robottini Mercenari"
# PARTIAL SOLUTION
# Maria Chiara Lischi, Matteo Spadaccia
#####

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

def greedy_loss_based(inputs_dict, connections_dict):
    # GREEDY SOLUTION
    cycle_inputs = inputs_dict.copy()
    selected_dict = {}
    while cycle_inputs != {}:
    
        # takes from the keys of the old dictionary the nodes that actually exist
        temp = {}
        for ii in cycle_inputs.keys():
            temp[ii] = connections_dict[ii]

        # creating dictionary "acutal_connections_dict" containing for each integer of input the other integers that choosing it would cut
        actual_connections_dict = {} 
        for ii in cycle_inputs.keys():
            actual_connections_dict[ii] = []
            for jj in temp[ii]:
                if jj in cycle_inputs.keys():
                    actual_connections_dict[ii] = actual_connections_dict[ii]+[jj]
    
        # computing the potential gain that choosing each integer implies 
        gain_dict = cycle_inputs.copy()
        #for ii in gain_dict.keys():
            #gain_dict[ii] = gain_dict[ii]*2
        for ii in cycle_inputs.keys():
            for jj in actual_connections_dict[ii]:
                gain_dict[ii] -= cycle_inputs[jj]
    
        # adding the item with maximum potential gain (minimum loss) to the dictionary
        max_gain_int = max(gain_dict, key = gain_dict.get)
        selected_dict[max_gain_int] = cycle_inputs[max_gain_int]
    
        # removing the integer with maximum potential gain (minimum loss) and the connected integers from input before the next iteration
        for ii in actual_connections_dict[max_gain_int]:
            cycle_inputs.pop(ii)
            
    return(list(selected_dict.keys()), sum(list(selected_dict.values())))

def greedy_value_minus_loss_based(inputs_dict, connections_dict):
    # GREEDY SOLUTION
    cycle_inputs = inputs_dict.copy()
    selected_dict = {}
    while cycle_inputs != {}:
    
        # takes from the keys of the old dictionary the nodes that actually exist
        temp = {}
        for ii in cycle_inputs.keys():
            temp[ii] = connections_dict[ii]

        # creating dictionary "acutal_connections_dict" containing for each integer of input the other integers that choosing it would cut
        actual_connections_dict = {} 
        for ii in cycle_inputs.keys():
            actual_connections_dict[ii] = []
            for jj in temp[ii]:
                if jj in cycle_inputs.keys():
                    actual_connections_dict[ii] = actual_connections_dict[ii]+[jj]
    
        # computing the potential gain that choosing each integer implies 
        gain_dict = cycle_inputs.copy()
        for ii in gain_dict.keys():
            gain_dict[ii] = gain_dict[ii]*2
        for ii in cycle_inputs.keys():
            for jj in actual_connections_dict[ii]:
                gain_dict[ii] -= cycle_inputs[jj]
    
        # adding the item with maximum potential gain (minimum loss) to the dictionary
        max_gain_int = max(gain_dict, key = gain_dict.get)
        selected_dict[max_gain_int] = cycle_inputs[max_gain_int]
    
        # removing the integer with maximum potential gain (minimum loss) and the connected integers from input before the next iteration
        for ii in actual_connections_dict[max_gain_int]:
            cycle_inputs.pop(ii)
            
    return(list(selected_dict.keys()), sum(list(selected_dict.values())))

def greedy_value_on_loss_n_based(inputs_dict, connections_dict):
    # GREEDY SOLUTION
    cycle_inputs = inputs_dict.copy()
    selected_dict = {}
    while cycle_inputs != {}:
    
        # takes from the keys of the old dictionary the nodes that actually exist
        temp = {}
        for ii in cycle_inputs.keys():
            temp[ii] = connections_dict[ii]

        # creating dictionary "acutal_connections_dict" containing for each integer of input the other integers that choosing it would cut
        actual_connections_dict = {} 
        for ii in cycle_inputs.keys():
            actual_connections_dict[ii] = []
            for jj in temp[ii]:
                if jj in cycle_inputs.keys():
                    actual_connections_dict[ii] = actual_connections_dict[ii]+[jj]
    
        # computing the potential gain that choosing each integer implies 
        gain_dict = cycle_inputs.copy()
        for ii in gain_dict.keys():
            #gain_dict[ii] = gain_dict[ii]*2
            gain_dict[ii]= gain_dict[ii]/len(actual_connections_dict[ii])
        #for ii in cycle_inputs.keys():
            #for jj in actual_connections_dict[ii]:
                #gain_dict[ii] -= cycle_inputs[jj]
    
        # adding the item with maximum potential gain (minimum loss) to the dictionary
        max_gain_int = max(gain_dict, key = gain_dict.get)
        selected_dict[max_gain_int] = cycle_inputs[max_gain_int]
    
        # removing the integer with maximum potential gain (minimum loss) and the connected integers from input before the next iteration
        for ii in actual_connections_dict[max_gain_int]:
            cycle_inputs.pop(ii)
            
    return(list(selected_dict.keys()), sum(list(selected_dict.values())))

def greedy_value_on_loss(inputs_dict, connections_dict):
    # GREEDY SOLUTION
    cycle_inputs = inputs_dict.copy()
    selected_dict = {}
    while cycle_inputs != {}:
    
        # takes from the keys of the old dictionary the nodes that actually exist
        temp = {}
        for ii in cycle_inputs.keys():
            temp[ii] = connections_dict[ii]

        # creating dictionary "acutal_connections_dict" containing for each integer of input the other integers that choosing it would cut
        actual_connections_dict = {} 
        for ii in cycle_inputs.keys():
            actual_connections_dict[ii] = []
            for jj in temp[ii]:
                if jj in cycle_inputs.keys():
                    actual_connections_dict[ii] = actual_connections_dict[ii]+[jj]
    
        print(actual_connections_dict)
        # computing the potential gain that choosing each integer implies 
        gain_dict = cycle_inputs.copy()
        fraction_dict = {}
        for ii in cycle_inputs.keys():
            fraction_dict[ii] = -cycle_inputs[ii]
            for jj in actual_connections_dict[ii]:
                fraction_dict[ii] += cycle_inputs[jj]
        for ii in gain_dict.keys():
            if fraction_dict[ii] == 0:
                gain_dict[ii] = max(gain_dict) + 1
            else:
                gain_dict[ii] = gain_dict[ii]/fraction_dict[ii]
            
        # adding the item with maximum potential gain (minimum loss) to the dictionary
        max_gain_int = max(gain_dict, key = gain_dict.get)
        selected_dict[max_gain_int] = cycle_inputs[max_gain_int]
    
        # removing the integer with maximum potential gain (minimum loss) and the connected integers from input before the next iteration
        for ii in actual_connections_dict[max_gain_int]:
            cycle_inputs.pop(ii)
            
    return(list(selected_dict.keys()), sum(list(selected_dict.values())))

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
    greedy_solutions = []
    greedy_solutions.append(greedy_loss_based(models, connections))
    greedy_solutions.append(greedy_value_minus_loss_based(models, connections))
    greedy_solutions.append(greedy_value_on_loss_n_based(models, connections))
    greedy_solutions.append(greedy_value_on_loss(models, connections))
    res = max(greedy_solutions)
    # adattare la risoluzione per inserirla in "res"
    print(f"Case #{t+1}: {res}") # output parzialmente corretto