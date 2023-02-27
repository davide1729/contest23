#!/usr/bin/env python3

def shift(char, s):
	if (char.isupper()):
		result = chr((ord(char) + s-65) % 26 + 65)
	else:
		result = chr((ord(char) + s - 97) % 26 + 97)
	return result

T = int(input())

for t in range(T):
	input()
	numchars, numkeys = [ int(x) for x in input().strip().split(" ") ]
	s = input().strip()
	keys = [ int(x) for x in input().strip().split(" ") ]
	keylen = [ int(x) for x in input().strip().split(" ") ]
	finalkeys = []
	for k, l in zip(keys, keylen):
		finalkeys += [k] * l
	if len(finalkeys) == 0:
		print(f"Case #{t+1}: {s}")
		continue
	while len(finalkeys) <= len(s):
		finalkeys *= 2

	res = ""
	for c,i in zip(s, range(len(s))):
		res += shift(c, finalkeys[i])
	print(f"Case #{t+1}: {res}")
