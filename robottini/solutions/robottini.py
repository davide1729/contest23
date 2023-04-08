import itertools

def get_divisors(n):
    div = []
    for ii in range(2, int(n/2) + 1):
        if n % ii == 0:
            div.append(ii)
    div.append(n)
    return div

# PREPARATION BASING ON N ONLY

def prepare_connections(N):
    # creating dictionary "divisors_dict" containing for each integer up to 100 a list of its divisors
    divisors_dict = {}
    for ii in range(2, N+1):
        divisors_dict[ii] = get_divisors(ii)
    
    # creating dictionary "connections_dict" containing for each integer up to 100 a list of its divisors and their multiples
    connections_dict = divisors_dict.copy()
    for ii in range(2, N+1):
        for jj in divisors_dict[ii]:
            for kk in range(2,N+1):
                if (jj in divisors_dict[kk]) and (kk not in connections_dict[ii]):
                    connections_dict[ii] = connections_dict[ii]+[kk]
    
    return(connections_dict)


def greedy(inputs_dict, connections_dict):
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
        max_gain_int = max(gain_dict, key=gain_dict.get)
        selected_dict[max_gain_int] = cycle_inputs[max_gain_int]
    
        # removing the integer with maximum potential gain (minimum loss) and the connected integers from input before the next iteration
        for ii in actual_connections_dict[max_gain_int]:
            cycle_inputs.pop(ii)
            
    return(list(selected_dict.keys()), sum(list(selected_dict.values())))


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

I = 100
N = 10
V = 100
int_list = [ii for ii in range(2,I+1)]
value_list = [ii for ii in range(1,V+1)]

connections_dict = prepare_connections(I)

for nn in range(3, N+1):
    print("Cycle number: ", nn)
    int_possible_combinations = list(itertools.combinations(int_list, nn)) #to add repetition
    value_possible_combinations = list(itertools.combinations(value_list, nn)) #to add repetition
    value_possible_disposition = []
    for value_combination in value_possible_combinations:
        value_possible_disposition += list(itertools.permutations(value_combination))        
    for int_combination in int_possible_combinations:
        for value_disposition in value_possible_disposition:
            inputs_dict = {}
            for ii in range(nn):
                inputs_dict[int_combination[ii]] = value_disposition[ii]
                if greedy(inputs_dict,connections_dict)[1] != empirical(inputs_dict,connections_dict)[1]: #or set(greedy(inputs_dict,connections_dict)[0]) != set(empirical(inputs_dict,connections_dict)[0]):
                    print("Error:", inputs_dict, greedy(inputs_dict,connections_dict), empirical(inputs_dict,connections_dict))