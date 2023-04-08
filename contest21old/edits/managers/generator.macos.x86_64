#!/usr/bin/env python3

#
# Generatore Gara Luiss 2021
# Task n.3 "Edits"
# Michele Lizzit
#

import string
import random

MAXT = 20
MAXN1 = int(10**2.3)
MAXN2 = int(10**6) * 20

T = 5
# T = random.randint(1, MAXT)

print(T)

for t in range(T):
	if t == 0:
		N = 5
	elif t == 1:
		N = 100
	elif t == 2:
		N = 1000
	elif t == 3:
		N = MAXN1
	elif t == 4:
		N = MAXN2

	print("")

	res = []
	num_sym = random.randint(int(N*0.6), int((3*N)/4))
	SYMBOLS = ["[C]", "[C]", "[C]", "[C]", "[L]", "[L]", "[R]"]
	LETTERS = "abcdefghijklmnopqrstuvwxyz_"
	res.extend([ random.choice(SYMBOLS) for _ in range(num_sym) ])
	res.extend([ random.choice(LETTERS) for _ in range(N - num_sym) ])
	random.shuffle(res)
	res = "".join(res)
	print(res)
