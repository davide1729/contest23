#!/usr/bin/env python3

import numpy as np
def cercapot(B, P):
    dif = -P
    if np.sum(B) < P:
        return 0, len(B)-1
    for k in range(len(B)):
        for k1 in range(k+1, len(B)):
            somma = np.sum(B[k:k1+1])
            if (somma-P) < 0:
                if somma-P > dif:
                    indexs = k, k1
                    dif = somma-P
            elif somma-P > 0:
                if somma-P < abs(dif):
                    indexs = k, k1
                    dif = somma - P
                else:
                    break
            else:
                indexs = k, k1
                dif = somma - P
                break
        if dif == 0:
            break
    return(indexs)


ncases = int(input())
for case in range(ncases):
    input()
    firstline = input()
    N, P = firstline.split(" ")
    N = int(N)
    P = int(P)
    secondline = input()
    batar = [int(x) for x in secondline.split(" ")]
    npbat = np.array(batar)
    a, b = cercapot(npbat, P)
    print(f"case #{case+1}: {a} {b}")
