#!/usr/bin/env python3

T = float(input())
assert T == int(T)
T = int(T)
assert 0 < T <= 100

for t in range(T):
    assert input() == ""
    N, M, k = input().strip().split(" ")
    N, M, k = float(N), float(M), float(k)
    assert N == int(N)
    assert M == int(M)
    assert k == int(k)
    N, M, k = int(N), int(M), int(k)
    assert 2 <= N <= 10**3
    assert 1 <= M <= 10**4
    assert 2 <= k <= 10
    for m in range(M):
      V = input().strip().split(" ")
      assert k == len(V)
      for v in V:
        assert float(v) == int(v)
        assert 0 <= int(v) <= N-1
