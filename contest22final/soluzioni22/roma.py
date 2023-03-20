#!/usr/bin/env python3

#
# Soluzione "Roma"
#

import sys
sys.setrecursionlimit(15000)

T = int(input())


def seen(x, y, matrix):
    matrix[x][y][1] = True
    if matrix[x][y][0] == 0:
        return
    if not matrix[x - 1][y][1]:
        seen(x - 1, y, matrix)
    if not matrix[x + 1][y][1]:
        seen(x + 1, y, matrix)
    if not matrix[x - 1][y - 1][1]:
        seen(x - 1, y - 1, matrix)
    if not matrix[x - 1][y + 1][1]:
        seen(x - 1, y + 1, matrix)
    if not matrix[x + 1][y - 1][1]:
        seen(x + 1, y - 1, matrix)
    if not matrix[x + 1][y + 1][1]:
        seen(x + 1, y + 1, matrix)
    if not matrix[x][y + 1][1]:
        seen(x, y + 1, matrix)
    if not matrix[x][y - 1][1]:
        seen(x, y - 1, matrix)

for t in range(T):
    input()
    N, M = tuple(int(i) for i in input().strip().split(' '))
    matrix = [[[0, False]]*(M + 2)]
    for i in range(N):
        row = [[0, False]] + list([int(i), False] for i in input().strip().split(' ')) + [[0, False]]
        matrix.append(row)
    matrix.append([[0, False]]*(M + 2))
    count = 0
    for x in range(1, N + 1):
        for y in range(1, M + 1):
            if matrix[x][y][0] == 1 and (not matrix[x][y][1]):
                seen(x, y, matrix)
                count += 1
    print(f"Case #{t + 1}: {count - 1}")
