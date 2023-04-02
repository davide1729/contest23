# Leonardo Azzi, Soluzione v1:
# Possible changes:
#   import blist?
#   use a list of lists instead of a dict?  (dict is faster, but list is more memory efficient)

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
            cursor_index[1] = max(0, cursor_index[1] - 2)
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

test = r"1{_}{_}89{<}{<}7{^}5{<}4{>}{>}6{^}23"
print(decoder(test)) # -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]