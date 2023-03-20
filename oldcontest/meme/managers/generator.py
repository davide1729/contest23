#!/usr/bin/env python3

#
# Generatore Gara Luiss 2021
# Task n.2 "Meme"
# Michele Lizzit
#

import string
import random

MAXN = 1000
MAXM = 1000
MAXQ = 100
MAXP = 1000

T = 20

print(T)

for t in range(T):
	N = random.randint(10, MAXN)
	M = random.randint(10, MAXM)

	if t == 0:
		N = 5
	elif t == 1:
		N = 100
	elif t == 2:
		N = 1000
	elif t == 3:
		N = MAXN
	elif t == 4:
		N = MAXN

	print("")
	print(f"{N} {M}")

	elems = [ (random.randint(1, M), random.randint(1, MAXQ)) ]
	for _ in range(N - 1):
		p = random.randint(1, MAXP)
		q = random.randint(1, MAXQ)
		elems.append((p, q))

	for elem in elems:
		print(f"{elem[0]} {elem[1]}")
