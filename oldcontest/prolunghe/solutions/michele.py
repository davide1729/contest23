#!/usr/bin/env python3

#
# Soluzione Gara Luiss 2021
# Task n.4 "Prolunghe"
# Michele Lizzit
#

T = int(input())

for t in range(T):
    input()
    N = int(input())
    s = [ x for x in input() ]
    pcs = [ int(x) for x in input().split() ]
    cor = [ pcs[i] for i in range(len(s)) if s[i] == "1" ]

    pcs.sort()
    cor.sort()

    res = 0

    if len(cor) == 1:
        for pc in pcs:
            res += abs(cor[0] - pc)
        print(f"Case #{t}: {res}")
        continue
    
    cur_i = 0
    for pc in pcs:
        res += min( abs(pc - cor[cur_i]) , abs(cor[cur_i + 1] - pc) )
        # print(f"{ pc - cor[cur_i]} {pc} {cor[cur_i + 1] - pc }: {min( abs(pc - cor[cur_i]) , abs(cor[cur_i + 1] - pc) )}")
        if cor[cur_i + 1] == pc and cur_i + 2 < len(cor):
            cur_i += 1

    print(f"Case #{t+1}: {res}")
    # break