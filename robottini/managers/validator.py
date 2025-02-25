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
    assert 1 < M <= 300
    models = input().strip().split(" ")
    assert len(models) == N
    powers = input().strip().split(" ")
    assert len(powers) == N
    for m in models:
        assert models.count(m) <= 1
        m = float(m)
        assert m == int(m)
        m = int(m)
        assert 1 < m <= M
    for p in powers:
        assert powers.count(p) <= 1
        p = float(p)
        assert p == int(p)
        p = int(p)
        assert 0 <= p <= 1000