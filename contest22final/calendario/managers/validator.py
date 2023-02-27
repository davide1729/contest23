#!/usr/bin/env python3

# Validator Task 3: Calendario accademico 
# Lorenzo Organtini | Mattia Cervellini

T = float(input())
assert T == int(T)
T = int(T)
assert 0 <= T <= 50
for t in range(T):
    assert input() == ""
    N, K = input().strip().split(" ")
    N, K = float(N), float(K)
    assert N == int(N)
    assert K == int(K)
    N, K = int(N), int(K)
    assert 0 <= N <= 10**7
    assert 0 <= K <= N
    LISTDAYS = input().strip().split(" ")
    assert N == len(LISTDAYS)
    for x in LISTDAYS:
        assert float(x) == int(x)
        x = int(x)
        assert 0 <= x <= 10**7

