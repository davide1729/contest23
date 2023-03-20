#!/usr/bin/env python3

#
# Generatore Gara Luiss 2021
# Task n.5 "Volo"
# Michele Lizzit
#

import string
import random

T = 20

print(T)

for t in range(T):
	MAXN = 1000
	MAXX = 1000
	MAXY = 1000
	MAXH = 10000
	MAXD = 100

	N = random.randint(50, MAXN)
	D = random.randint(1, MAXD)
	if t == 0:
		N = 5
	elif t == 1:
		N = 10
	elif t == 2:
		N = 15
	elif t == 3:
		N = 20
	elif t == 4:
		N = 25

	print("")

	nodelist = set()
	if t == 0:
		N = 10
		D = 100
	elif t == 1:
		N = 100
		D = 50
	elif t == 2:
		N = 1000
		D = 40
	elif t == 3:
		N = 1000
		D = 30
	elif t == 4:
		N = 1000
		D = 20
	elif t == 5:
		N = 1000
		D = 20
	elif t < 10:
		D = 100
		N = 1000
		MAXX = 100
		MAXY = 100
	elif t < 13:
		print("1000 100")
		for i in range(1000):
			if i <= 500:
				print(f"{i+1} 1 {2000 - 2*(i+1)}")
			else:
				print(f"{i+1} 1 {(i*2) - 3}")
		continue

	for _ in range(N):
		x = random.randint(1, MAXX)
		y = random.randint(1, MAXY)
		h = random.randint(1, MAXH)
		nodelist.add((x, y, h))

	nodelist = list(nodelist)
	random.shuffle(nodelist)

	print(f"{N} {D}")

	for a,b,c in nodelist:
		print(f"{a} {b} {c}")
