#!/usr/bin/env python3

T = int(input())

for t in range(T):
    input()
    N, P = input().strip().split(" ")
    N, P = int(N), int(P)
    l = [int(x) for x in input().strip().split(" ")]

    cur = l[0]
    i, j = 0, 0
    end = False
    best = i, j, cur
    while not end:
        if cur < P and j < N - 1:
            j += 1
            cur += l[j]
        elif cur > P and i < j:
            cur -= l[i]
            i += 1
        elif cur > P and i == j and j < N - 1:
            j += 1
            cur += l[j]
            cur -= l[i]
            i += 1
        else:
            end = True
        if abs(cur - P) < abs(best[2] - P):
            best = i, j, cur
    print(f"Case #{t + 1}: {best[0]} {best[1]}")