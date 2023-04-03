"""
@author: Carlo Malagnino

Task: Edits
"""

from blist import blist

T=int(input())

for t in range(1,T+1):
    ln=input()
    ln=input()
    n=len(ln)
    p=0
    cmd=blist()
    c=0
    while(p<n):
        if ln[p]=="[":
            if(ln[p+1]=="C"):
                if(c>0):
                    del(cmd[c-1])
                    c-=1
            elif(ln[p+1]=="L"):
                c=max(0,c-1)
            else:
                c=min(len(cmd),c+1)
            p+=3
        else:
            cmd.insert(c,ln[p])
            p+=1
            c+=1
    print("Case #{}: {}".format(t,''.join(cmd)))
