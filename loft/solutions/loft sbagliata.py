#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 4 "Breaking into LOFT"
# CORRECT SOLUTION
# Francesca Romana Sanna, Leonardo Azzi
#####

# Leonardo Azzi, Soluzione v1:
# Possible changes:
#   import blist?
#   use a list of lists instead of a dict?  (dict is faster, but list is more memory efficient)

T = int(input()) # numero di casi di test

def decoder(test):
    matrix = {}
    cursor_index = [0, 0]
    for i in test:
        if i == '{' or i == '}':
            continue
        elif i == '_':
            cursor_index[0] += 1
            matrix[cursor_index[0]] = matrix.get(cursor_index[0], [])
            cursor_index[1] = min(len(matrix.get(cursor_index[0], [])), cursor_index[1])
            #Se necessario, implementare un cap massimo di "profondità" (usa min(max_depth, cursor_index[0] + 1))
        elif i == '^':
            cursor_index[0] = max(0, cursor_index[0] - 1)
            matrix[cursor_index[0]] = matrix.get(cursor_index[0], [])
            cursor_index[1] = min(len(matrix.get(cursor_index[0], [])), cursor_index[1])
        elif i == '>':
            cursor_index[1] = min(len(matrix.get(cursor_index[0], [])), cursor_index[1] + 1)
        
    result = []
    for n in range(len(matrix)):
        result.append(matrix.get(n, []))
    return result

for t in range(T):
    input() # spazio
    test = input()
    print(f"Case #{t+1}: {decoder(test)}")