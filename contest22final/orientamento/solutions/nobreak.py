#!/usr/bin/env python3
# Matteo Spadaccia
 
def maxANBf (N, P, a, x): 
    A = a
    y = (100*x)/(100+x)

    for i in range(N-1):
        b = (a*(100+x)/100)
        if b <= P:
            a = b
        else:
            a = a*(100-y)/100
        A += a
        
    return int(A)

for case in range(20):
    input()
    N, P, a, x = input().strip().split(" ")
    N, P, a, x = int(N), int(P), int(a), int(x)
    sol = maxANBf (N, P, a, x)
    print(f"Case #{case + 1}: {sol}")