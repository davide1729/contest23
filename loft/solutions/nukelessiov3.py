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
            cursor_index[0] = cursor_index[0] + 1
            matrix[cursor_index[0]] = matrix.get(cursor_index[0], [])
            cursor_index[1] = min(len(matrix[cursor_index[0]]), cursor_index[1])
            #Se necessario, implementare un cap massimo di "profondità" (usa min(max_depth, cursor_index[0] + 1))
        elif i == '^':
            cursor_index[0] = max(0, cursor_index[0] - 1)
            matrix[cursor_index[0]] = matrix.get(cursor_index[0], [])
            cursor_index[1] = min(len(matrix[cursor_index[0]]), cursor_index[1])
        elif i == '>':
            cursor_index[1] = min(len(matrix[cursor_index[0]]), cursor_index[1] + 1)
        elif i == '<':
            cursor_index[1] = max(0, cursor_index[1] - 1)
            #print(f"Cursor index: {cursor_index[1]}")
        elif i.isdigit():
            matrix[cursor_index[0]] = matrix.get(cursor_index[0], [])
            matrix[cursor_index[0]].insert(cursor_index[1], int(i))
            cursor_index[1] += 1
            #print(matrix)
    result = []
    for n in range(len(matrix)):
        result.append(matrix[n])
    return result

for t in range(T):
    input() # spazio
    test = input()
    print(f"Case #{t+1}: {decoder(test)}")



# test_list = {r"1{>}2{_}3{>}4{<}5{>}6{<}7{>}8{<}9" : [[1,2],[3,5,4,7,6,9,8]],
# r"1{>}23{_}4{>}56{_}7{>}89" : [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
# r"1{_}23{^}4{_}56{^}7{_}89" : [[1, 4, 7], [2, 3, 5, 8, 9, 6]],
# r"1{>}2{>}3{<}{_}4{>}5{>}6{<}{_}7{>}8{>}9" : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}

# for tests in test_list:
#     print(f"Test: {tests}\n")
#     print(f"Expected: {test_list[tests]}\n")
#     print(f"Result: {decoder(tests)}\n")
#     print(f"Passed: {decoder(tests) == test_list[tests]}\n")
#     print()

