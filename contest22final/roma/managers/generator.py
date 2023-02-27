#!/usr/bin/env python3
# Generatore
# Task "Roma"
# Carlo Malagnino


import random

MAXT = 25
MAXN = 300

print(MAXT)
print()

N = random.randint(2, 10)
M = random.randint(2, 10)
print("{} {}".format(N, M))
  
for i in range(N):
  for j in range(M):
    m= random.randint(0, 1)
    print(m, end=' ')
  print()

for t in range(4):
  print()
  N = random.randint(11, 100)
  M = random.randint(11, 100)
  print("{} {}".format(N, M))
  
  for i in range(N):
    for j in range(M):
      m= random.randint(0, 1)
      print(m, end=' ')
    print()


for t in range(20):
  print()
  N = random.randint(101, MAXN)
  M = random.randint(101, MAXN)
  print("{} {}".format(N, M))
  
  for i in range(N):
    for j in range(M):
      m= random.randint(0, 1)
      print(m, end=' ')
    print()
