#!/usr/bin/env python3

# 
# Validator Final Contest LUISSMatics 2022
# Task n. 1 "Café Cypher (cifrario)"
# Demetrio Cardile, Davide Beltrame
#

import string

T = float(input())
assert T == int(T)
T = int(T)
assert 0 <= T <= 25
for t in range(T):
    assert input() == ""
    N, K = input().strip().split(" ")
    N, K = float(N), float(K)
    assert N == int(N)
    assert K == int(K)
    N, K = int(N), int(K)
    assert 0 <= N <= 10**4
    assert 0 <= K <= N
    S = input()
    assert S == str(S)
    assert len(S) == int(N)
    for letter in S:
        assert letter in string.ascii_letters
    if K != 0:
        keys = input().strip().split(" ")
        assert int(len(keys)) == int(K)
        for x in keys:
            assert float(x) == int(x)
            x = int(x)
            assert 0 <= x <= 1000
        chars = input().strip().split(" ")
        for x in chars:
            assert float(x) == int(x)
            x = int(x)
            assert 0 <= x <= N