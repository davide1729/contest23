#!/usr/bin/env python3

#Solution Mutanti Tuned for 25/100

T=int(input())

for t in range(T):
    input()
    
    N,M,K=[int(x) for x in input().strip().split(' ')]
    
    seq={}
        
    for i in range(N):
        seq[i]=[]
        
    for m in range(M):
        l=[int(x) for x in input().strip().split(' ')]
            
        if l[0]>=l[1]:
            seq[l[1]].append(l[0])

    if K==2:
        sol=True   
        res=2
            
        for i in range(N):
            if len(seq[i])==0:
                sol=False
        if sol:
            for i in range(1,N):
                if i-1 in seq[i]:
                    res+=1
                else:
                    res+=2
        
            print(f"Case #{t+1}: {res}")
        else:
            print(f"Case #{t+1}: -1")
                
    #else:
    #    print(f"Case #{t+1}: -2")