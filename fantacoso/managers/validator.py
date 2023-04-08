#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. x "fantacos"
# INPUT VALIDATOR
# Michele Turco, Chiara Baldoni
#####

T = float(input()) # 25
assert T == int(T)
T = int(T)
assert 0 <= T <= 25
for t in range(T):
    assert input() == ""
    assert len(input())==7
    ln=input().split()
    for element in ln:
        assert element==int(element)
    K=int(ln[0])
    for row in range(K):
        assert len(input())==5
        data=input().split()
        for element in data:
            assert element==int(element)