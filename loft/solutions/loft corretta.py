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
    # Remove brackets
    test = test.replace('{', '').replace('}', '')

    # Ignore consecutive '^' commands at the beginning
    while test and test[0] == '^':
        test = test[1:]
        
    if test == "":
        return []
    
    matrix = {0: []}
    cursor_index = [0, 0]
    
        
    for i in test:
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
    result = []
    
    if len(matrix) == 1:
        return matrix[0]
    
    for n in range(len(matrix)):
        result.append(matrix.get(n, []))
    return result

for t in range(T):
    input() # spazio
    test = input()
    print(f"Case #{t+1}: {decoder(test)}")

# Manual tests
# test_list = {r"1{>}2{_}3{>}4{<}5{>}6{<}7{>}8{<}9" : [[1,2],[3,5,4,7,6,9,8]],
# r"1{>}23{_}4{>}56{_}7{>}89" : [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
# r"1{_}23{^}4{_}56{^}7{_}89" : [[1, 4, 7], [2, 3, 5, 8, 9, 6]],
# r"1{>}2{>}3{<}{_}4{>}5{>}6{<}{_}7{>}8{>}9" : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# }

# for tests in test_list:
#     print(f"Test: {tests}\n")
#     print(f"Expected: {test_list[tests]}\n")
#     print(f"Result: {decoder(tests)}\n")
#     print(f"Passed: {decoder(tests) == test_list[tests]}\n")
#     print()