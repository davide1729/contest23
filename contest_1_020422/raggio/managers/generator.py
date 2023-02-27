#!/usr/bin/env python3
import random

def human_doable():
	N = random.randint(1, 10)
	P = random.randint(1, 100)
	l = [ random.randint(1,99) for _ in range(N) ]
	print(f"{N} {P}")
	print(" ".join([ str(x) for x in l ]))

def big_int():
	N = random.randint(1, 100)
	P = random.randint(1, 10**12)
	l = [ random.randint(1,10**11) for _ in range(N) ]
	print(f"{N} {P}")
	print(" ".join([ str(x) for x in l ]))

def easy_points():
	N = random.randint(1, 1000)
	P = random.randint(1, 1000)
	l = [ random.randint(1,100) for _ in range(N) ]
	print(f"{N} {P}")
	print(" ".join([ str(x) for x in l ]))

def rompi_quadratiche():
	N = 2 * 10**5 + random.randint(-1000, 1000)
	l = [ random.randint(1,10**3) for _ in range(N) ]
	P = sum(l) - 1
	print(f"{N} {P}")
	print(" ".join([ str(x) for x in l ]))

def edge_case():
	N = 10**5 + random.randint(-1000, 1000)
	l = [ random.randint(1,10**3) for _ in range(N) ]
	P = 10**9 + random.randint(-10000, -1)
	print(f"{N} {P}")
	print(" ".join([ str(x) for x in l ]))

def big_random():
	N = 10**6 + random.randint(-10000, 10000)
	l = [ random.randint(1,10**2) for _ in range(N) ]
	P = sum(l) - random.randint(1, 1000)
	print(f"{N} {P}")
	print(" ".join([ str(x) for x in l ]))


CASES = [human_doable] * 2 + [easy_points] * 4 + [big_int] * 3 + [ rompi_quadratiche ] * 6 + [ edge_case ] * 2 + [ big_random ] * 8

print(len(CASES))

for x in CASES:
	print()
	x()
