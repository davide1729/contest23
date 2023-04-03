#!/usr/bin/env python3
import math

T = float(input())
assert T == int(T)
T = int(T)
assert 0 <= T <= 100

for t in range(T):
    assert input() == ""
    C = float(input())
    assert C == int(C)
    C = int(C)
    for c in range(C):
        L = input().strip().split(" ")
        N = float(L.pop(0))
        assert N == int(N)
        N = int(N)
        assert len(L) == N
        assert N <= 100000
        assert math.log(N + 1, 2) == int(math.log(N + 1, 2))
        for t_i in L:
            tt = float(t_i)
            assert int(tt) == tt
            assert tt <= 100000
