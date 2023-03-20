#!/usr/bin/env python3

#
# Generatore Gara Luiss 2021
# Task n.1 "Quiz"
# Michele Lizzit
#

import string
import random

MAXT = 20
MAXN1 = 200
MAXN2 = 1000

T = 20
# T = random.randint(1, MAXT)

print(T)

for t in range(T):
	N = random.randint(50,MAXN1)
	if t > 17:
		N = random.randint(MAXN2 - 150,MAXN2)
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

	nodelist = []
	if t % 5 == 0:
		# Grafo denso
		for i in range(N):
			for j in range(N):
				nodelist.append((i, j))
	elif t % 5 == 1:
		# Grafo denso spaccato (toglie il 10% random degli archi)
		for i in range(N):
			for j in range(N):
				if random.randint(0, 10) != 0:
					nodelist.append((i, j))
	elif t % 5 == 2:
		# Grafo denso senza un arco
		for i in range(N):
			for j in range(N):
				nodelist.append((i, j))
		random.shuffle(nodelist)
		nodelist.pop()
	elif t % 5 == 3:
		# Due grafi densi non connessi
		nodes = [x for x in range(N)]
		random.shuffle(nodes)
		divisor = random.randint(1,len(nodes)-1)
		nodes1 = nodes[:divisor]
		nodes2 = nodes[divisor:]

		for i in nodes1:
			for j in nodes1:
				nodelist.append((i, j))
		for i in nodes2:
			for j in nodes2:
				nodelist.append((i, j))
	elif t % 5 == 4:
		# Grafo spaccatissimo (toglie il 70% random degli archi)
		for i in range(N):
			for j in range(N):
				if random.randint(0, 10) <= 3:
					nodelist.append((i, j))

	random.shuffle(nodelist)
	print(f"{N} {len(nodelist)}")

	for a,b in nodelist:
		print(f"{a} {b}")
