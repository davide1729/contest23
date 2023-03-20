#!/usr/bin/env python3

"""
@author: Carlo Malagnino

Task: meme
"""

T=int(input())

for t in range(1,T+1):
    ln=input()
    ln=input().split()
    N=int(ln[0])
    m=int(ln[1])
    
    w=[0]
    p=[0]
    
    for i in range(N):
        ln=input().split()
        w.append(int(ln[0]))
        p.append(int(ln[1]))
    
    M = [ [ (0,-1) for i in range(m+1) ] for j in range(N+1) ]
    
    for i in range(1,N+1):
        for j in range(m+1):
            if(w[i]>j):
                M[i][j]=M[i-1][j]
            else:
                if(p[i]+M[i-1][j-w[i]][0]>M[i-1][j][0]):
                    M[i][j]=(p[i]+M[i-1][j-w[i]][0], i)
                else:
                    M[i][j]=M[i-1][j]
    g=N
    h=m
    ris=[]
    '''
    for i in range(0,N+1):
        for j in range(m+1):
            print(M[i][j], end=" ")
        print()
    '''
    while(M[g][h][1]!=-1):
        meme=M[g][h][1]
        ris.append(meme)
        h-=w[meme]
        g=meme-1
    ris.reverse()
    print("Case #{}: ".format(t), end="")
    for e in ris:
        print(e, end=" ")
    print()
