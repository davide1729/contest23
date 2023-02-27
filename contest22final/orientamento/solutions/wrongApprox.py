#!/usr/bin/env python3
# Matteo Spadaccia

def maxAWAf (N, P, a, x): 
    A = a
    maxa = 0
    y = (100*x)/(100+x)
    flag = False
    
    for i in range(N-1):
        b = (a*(100+x)/100)
        if b <= P:
            a = b
            A += a
        elif maxa == a:
            flag = True
            break            
        else:
            maxa = a
            b = a*(100-y)/100
            a = b
            A += a
    
    if flag and (N-1-i)%2 == 0:
        A += ((N-1-i)/2)*a
        b = a*(100-y)/100
        a = b
        A += ((N-1-i)/2)*a
    elif flag:
        A += (((N-1-i)-1)/2)*a
        b = a*(100-y)/100
        a = b
        A += (((N-1-i)+1)/2)*a
        
    return int(A)

for case in range(50):
    input()
    N, P, a, x = input().strip().split(" ")
    N, P, a, x = int(N), int(P), int(a), int(x)
    sol = maxAWAf (N, P, a, x)
    print(f"Case #{case + 1}: {sol}")