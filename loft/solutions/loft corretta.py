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


def decoder(leo):
    # Remove brackets
    leo = leo.replace('{', '').replace('}', '')

    # Ignore consecutive '^' commands at the beginning
    while leo and leo[0] == '^':
        leo = leo[1:]
        
    if leo == "":
        return []
    
    matrix = {0: []}
    cursor_index = [0, 0]
    
        
    for i in leo:
        if i == '_':
            cursor_index[0] += 1
            matrix[cursor_index[0]] = matrix.get(cursor_index[0], [])
            cursor_index[1] = min(len(matrix.get(cursor_index[0], [])), cursor_index[1])
        elif i == '^':
            cursor_index[0] = max(0, cursor_index[0] - 1)
            matrix[cursor_index[0]] = matrix.get(cursor_index[0], [])
            cursor_index[1] = min(len(matrix.get(cursor_index[0], [])), cursor_index[1])
        elif i == '>':
            cursor_index[1] = min(len(matrix.get(cursor_index[0], [])), cursor_index[1] + 1)
        elif i == '<':
            cursor_index[1] = max(0, cursor_index[1] - 1)
        elif i.isdigit():
            matrix[cursor_index[0]] = matrix.get(cursor_index[0], [])
            matrix[cursor_index[0]].insert(cursor_index[1], int(i))
            cursor_index[1] += 1
    risultato_corretto = []
    
    if len(matrix) == 1:
        return matrix[0]
    
    for n in range(len(matrix)):
        risultato_corretto.append(matrix.get(n, []))
    return risultato_corretto

T = int(input()) # numero di casi di test

for t in range(1, T+1):
    input() # spazio
    test = input()
    print(f"Case #{t}: {decoder(test)}")
