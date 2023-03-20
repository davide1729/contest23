#!/usr/bin/env python3

#
# Soluzione Gara Luiss 2021
# Task n.3 "Edits"
# Michele Lizzit
#

from blist import blist

T = int(input())

for t in range(T):
    input()
    inp = input().replace("[L]", "<").replace("[R]", ">").replace("[C]", "!")
    res = blist()
    poi = 0
    for e in inp:
        if poi == 0 and (e == "<" or e == "!"):
            continue
        if len(res) == poi and e == ">":
            continue
        if e == "<":
            poi -= 1
            continue
        if e == ">":
            poi += 1
            continue
        if e == "!":
            poi -= 1
            del res[poi]
            continue
        res.insert(poi, e)
        poi += 1
    res = "".join(res)
    print(f"Case #{t+1}: {res}")