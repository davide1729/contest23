#!/usr/bin/env python3

def destroy (i):
  global Boolean
  if (N-1)/2 <= i <= N-1:
    Boolean[i] = 0
    return 2
  elif (Boolean[2*i+1] == 0 and Boolean[2*i+2] == 0):
    Boolean[i] = 0
    return 2
  elif Boolean[2*i+1] == 0 and Boolean[2*i+2] == 1:
    Boolean[i] = 0
    return 2+destroy(2*i+2)
  elif Boolean[2*i+1] == 1 and Boolean[2*i+2] == 0:
    Boolean[i] = 0
    return 2+destroy(2*i+1)
  elif Boolean[2*i+1] == 1 and Boolean[2*i+2] == 1:
    Boolean[i] = 0
    return 2+destroy(2*i+2)+destroy(2*i+1)
    
  
T = int(input())
for t in range(T):
  input()
  print('Case #', t+1, ':', sep = '', end = '')
  C = int(input())
  for c in range(C):
    print(' ', end = '')
    L = [ int(x) for x in input().strip().split(" ") ]
    N = int(L.pop(0))
    Boolean = [1 for jj in range(len(L))]
    Zeros = [0 for ii in range(len(L))]
    flag = 0
    time = 0
    while Boolean != Zeros and flag == 0:
      m = 100001
      for ii in range(len(Boolean)):
        if Boolean[ii] == 1 and L[ii] < m:
          m = L[ii]
      i = L.index(m)
      time += destroy(i)
      if m < time:
        flag = 1
    if flag == 1:
        print('Luiss_LOFT', end = '')
    if flag == 0:
        print('Droni_disattivati', end = '')
  print('')
