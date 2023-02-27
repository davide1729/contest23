#!/usr/bin/env python3

moves = []
drones, nMoves, length = 0, 0, 0

def distance(a, b):	
	endA = moves[a][length - 1]
	for st in range(length + 1):
		fail = False
		for i in range(length - st):
			if (moves[a][st + i] != moves[b][i]):
				fail = True
				break;
		if not fail:
			for i in range(length - st, length):
				if (moves[b][i] <= endA):
					fail = True;
			if (fail):
				continue;
			return st;
	return -1;

def test():
	global moves;
	global drones, nMoves, length;
	drones, nMoves, length = input().strip().split(" ")
	drones, nMoves, length = int(drones), int(nMoves), int(length)
	moves = []
	moves.append([ -1 for _ in range(length) ])
	hMoves = [ [] for _ in range(drones + 1) ]
	for i in range(1, nMoves + 1):
		p = []
		p = [ int(x) for x in input().strip().split(" ") ]
		hMoves[p[length - 1]].append(i);		
		moves.append(p);
	q = set()
	seen = [False for _ in range(nMoves + 1) ]
	
	q.add((0, 0, 0))
	
	while len(q) > 0:
		s = max(q)
		q.remove(s)
		if (seen[s[2]]): continue;
		seen[s[2]] = True;
		if (s[1] == drones):
			print(s[0])
			return;
		for m in hMoves[s[1]]:
			if (seen[m]): continue;
			dist = distance(s[2], m);
			if (dist >= 0):
				q.add((s[0] + dist, s[1] + 1, m));
	print("-1")

def main():
	t = int(input());
	for i in range(t):
		print(f"Case #{i+1}: ", end="")
		input()
		test()

main()