#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 4 "Robottini Mercenari"
# INPUT VALIDATOR
# Davide Beltrame
#####

T = float(input()) # 25
assert T == int(T)
T = int(T)
assert 0 <= T <= 25
for t in range(T):
    assert input() == "" # spazio vuoto
    N = float(input())
    assert N == int(N)
    N = int(N)
    assert 0 < N <= 150
    M = float(input())
    assert M == int(M)
    M = int(M)
    assert 0 < M <= 1000
    models = input().strip().split(" ")
    assert len(models) == N
    powers = input().strip().split(" ")
    assert len(powers) == N
    for m in models:
        m = int(m)
        assert 2 <= m <= M
    for p in powers:
        p = int(p)
        assert 0 <= p <= 1000
