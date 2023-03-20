#!/usr/bin/env python3

#
# Soluzione Gara Luiss 2021
# Task n.1 "Quiz"
# Michele Lizzit
# (porting della soluzione armando.cpp)
#

def dfs(u, c):
    colore[u] = c
    for v in adj[u]:
        if(colore[u]==colore[v] ):
            return False
        elif (colore[v] == -1) and (not dfs(v,1-c) ):
            return False
    return True

T = int(input())

for t in range(T):
    input()
    N, M = [int(x) for x in input().split(" ")]
    mat = [[0 for x in range(N)] for _ in range(N)]    
    colore = [-1 for x in range(N)]
    adj = [[] for x in range(N)]
    n, m = N, M

    for i in range(M):
        a, b = [int(x) for x in input().split(" ")]
        mat[a][b] = 1
        mat[b][a] = 1

    for i in range(N):
        for j in range(N):
            if i!=j and (not mat[i][j]):
                adj[i].append(j)

    ok = True

    for i in range(n):
        if colore[i] == -1:
            if not dfs(i,0):
                ok = False

    if not ok:
        print(f"Case #{t+1}: -1")
    elif len(set(colore)) == 1:
        print(f"Case #{t+1}: 1 0 {n-1}", end=" ")
        for i in range(1, n):
            print(i, end=" ")
        print()
    else:
        n1, n2 = 0, 0
        print(f"Case #{t+1}:", end=" ")

        for i in range(n):
            if (colore[i]==0):
                n1+=1
            else:
                n2+=1
        print(n1, end=" ")
        for i in range(n):
            if(colore[i]==0):
                print(i, end=" ")
        print(n2, end=" ")
        for i in range(n):
            if(colore[i]==1):
                print(i, end=" ")
        print()