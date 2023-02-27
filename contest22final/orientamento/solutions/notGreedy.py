#!/usr/bin/env python3
# Matteo Spadaccia

def maxAngf (P,x,y,s,e):
    global BB
    global B
    if s >= e:
        return
    else:
        m = s+((e-s)+1)//2
        for i in range(s,m):
            b = B[i]*(100-y)/100
            B[i] = b
            BB[i] += B[i]
        for i in range(m,e+1):
            b = B[i]*(100+x)/100
            if b <= P:
                B[i] = b
                BB[i] += B[i]
            else:
                BB[i] = -1
                B[i] = -1
        if ((e-s)+1)/2 == int(((e-s)+1)/2):
            maxAngf (P,x,y,s,m-1)
            maxAngf (P,x,y,m,e)

BB = []
B = []
def maxANG (N, P, a, x):
    global BB
    global B
    BB = []
    B = []
    y = (100*x)/(100+x)
    for i in range(2**(N-1)):
        BB.append(a)
        B.append(a)
    maxAngf (P,x,y,0,2**(N-1)-1)
    return int(max(BB))

for case in range(0):
    input()
    N, P, a, x = input().strip().split(" ")
    N, P, a, x = int(N), int(P), int(a), int(x)
    sol = maxANG (N, P, a, x)
    print(f"Case #{case + 1}: {sol}")