#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 3 "PageRank"
# INPUT VALIDATOR
# Demetrio F. Cardile, Davide Beltrame
#####

T = float(input()) # 25
assert T == int(T)
T = int(T)
assert 0 <= T <= 25
a = float(input()) # alpha
assert a == int(a)
a = int(a)
assert 0 <= a <= 9
for t in range(T):
    assert input() == "" # spazio vuoto
    # controlla tutti gli altri
    N = float(input())
    assert N == int(N)
    N = int(N)
    assert 0 < N <= 2000
    for i in range(N):
        nodes = input().strip().split(" ")
        print(nodes)
        node_name = int(nodes[0])
        assert node_name < N
        length = int(len(nodes))
        #print(length)