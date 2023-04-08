#!/usr/bin/env python3

# 2
#
# 2
# 7 7 6 5 1 2 8 9
# 3 3 1 1
#
# 1
# 3 20 2 5

cnt = 0

def destroy(i, todo):
    if i not in todo:
        return True

    global cnt
    tt = i[0]
    i = i[1]
    
    if i*2+2 <= N:
        a = (l[2*i+1], 2*i+1)
        b = (l[2*i+2], 2*i+2)

        if not (destroy(a, todo) and destroy(b, todo)):
            return False

    cnt += 2
    todo.remove((tt, i))
    if cnt <= tt:
        return True
    else:
        return False


T = int(input())

for t in range(T):
    input()
    C = int(input())
    print(f"Case #{t+1}:", end="")
    for c in range(C):
        cnt = 0
        l = [ int(x) for x in input().strip().split(" ") ]
        N = l[0]
        l = l[1:]
        l2 = [ (l[i],i) for i in range(len(l)) ]
        todo = set(l2)
        done = True
        while len(todo) > 0:
            v = todo.pop()
            todo.add(v)
            if not destroy(v, todo):
                done = False
                break
        if done:
            print(f" Droni_disattivati", end="")
        else:
            print(f" Luiss_LOFT", end="")
    print()