#!/usr/bin/env python3

T = float(input())
assert T == int(T)
T = int(T)
assert 0 <= T <= 50

for t in range(T):
    assert input() == ""
    N, P = input().strip().split(" ")
    N, P = float(N), float(P)
    assert N == int(N)
    assert P == int(P)
    N, P = int(N), int(P)
    assert 0 <= N <= 10**7
    assert 0<= P <= 10**12
    for x in input().strip().split(" "):
        assert float(x) <= 10**12
