#!/usr/bin/env python3

T = int(input())

for t in range(T):
    input()
    N, P = input().strip().split(" ")
    N, P = int(N), int(P)
    l = [int(x) for x in input().strip().split(" ")]

    start=0
    end=0
    sum=l[0]
    opt=abs(sum-P)
    x,y=0,0

    while(start<N and end<N):
        if sum<P:
            end+=1
            if end==N:
                break
            sum+=l[end]
            if opt>abs(sum-P):
                opt,x,y=abs(sum-P),start,end
        elif sum>P:
            sum-=l[start]
            start+=1
            if start<=end and opt>abs(sum-P):
                opt,x,y=abs(sum-P),start,end
        else:
            break
    
    print(f"Case #{t + 1}: {x} {y}")