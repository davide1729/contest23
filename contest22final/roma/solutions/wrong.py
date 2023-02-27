#!/usr/bin/env python3

# Wrong
# "Roma"
#

import sys
sys.setrecursionlimit(250000)

T = int(input())

matrix = [[[0, False]]*600]*600
def seen(x, y):
    matrix[x][y][1] = True
    if matrix[x][y][0] == 0:
        return
    else:
        if not matrix[x - 1][y][1]:
            seen(x - 1, y)
        if not matrix[x + 1][y][1]:
            seen(x + 1, y)
        if not matrix[x - 1][y - 1][1]:
            seen(x - 1, y - 1)
        if not matrix[x - 1][y + 1][1]:
            seen(x - 1, y + 1)
        if not matrix[x + 1][y - 1][1]:
            seen(x + 1, y - 1)
        if not matrix[x + 1][y + 1][1]:
            seen(x + 1, y + 1)
        if not matrix[x][y + 1][1]:
            seen(x, y + 1)
        if not matrix[x][y - 1][1]:
            seen(x, y - 1)

for t in range(T):
    input()
    N, M = tuple(int(i) for i in input().strip().split(' '))
    for i in range(1, N + 1):
        row = list([int(i), False] for i in input().strip().split(' '))
        for j in range(1, M + 1):
            matrix[i][j] = row[j - 1]
    count = 0
    for x in range(1, N + 1):
        for y in range(1, M + 1):
            if matrix[x][y][0] == 1 and (not matrix[x][y][1]):
                seen(x, y)
                count += 1
    print(f"Case #{t + 1}: {count - 1}")
