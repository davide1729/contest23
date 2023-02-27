#!/usr/bin/env python3


T = float(input())
assert T == int(T)
T = int(T)
assert 0 < T <= 30

for t in range(T):
  assert input() == ""
  N = float(input())
  assert N == int(N)
  N = int(N)
  assert 1 <= N <= 50000
  x, y, a, b = input().strip().split(" ")
  x, y, a, b = float(x), float(y), float(a), float(b)
  assert x == int(x)
  assert y == int(y)
  assert a == int(a)
  assert b == int(b)
  x, y, a, b = int(x), int(y), int(a), int(b)
  assert x <= 2**51
  assert y <= 2**51
  assert a <= 2**51
  assert b <= 2**51
  for n in range(N):
    r, s, t, u = input().strip().split(" ")
    r, s, t, u = float(r), float(s), float(t), float(u)
    assert r == int(r)
    assert s == int(s)
    assert t == int(t)
    assert u == int(u)
    r, s, t, u = int(r), int(s), int(t), int(u)
    assert r <= 2**51
    assert s <= 2**51
    assert t <= 2**51
    assert u <= 2**51
