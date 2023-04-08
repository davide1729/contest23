#!/usr/bin/env python3

#
# Generatore Gara Luiss 2021
# Task n.4 "Prolunghe"
# Michele Lizzit
#

import string
import random

MAXN = 2000
MAXX = 200000

T = 80

print(T)

for t in range(T):
	N = random.randint(10, MAXN)

	if t == 0:
		N = 5
	elif t == 1:
		N = 10
	elif t == 2:
		N = 1000
	elif t == 3:
		N = MAXN
	elif t == 4:
		N = MAXN

	print("")
	print(f"{N}")
	s = [ "1" if random.randint(0,2) == 0 else "0" for _ in range(N) ]
	s[random.randint(0, len(s) - 1)] = "1"
	s = "".join(s)
	print(s)

	elems = [ str(random.randint(1, MAXX)) for _ in range(N) ]
	elems.sort()
	elems = " ".join(elems)
	print(elems)