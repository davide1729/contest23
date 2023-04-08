#!/usr/bin/env python3

# temp CHECKER SKELETON
# generated from code sections common to all checkers

#
# Checker Intermediate Contest LUISSMatics 2022
# Task n. 2 "Droni mutanti (mutanti)"
# Michele Lizzit, Davide Beltrame
#

from itertools import accumulate
from parser import Parser
from sys import argv, exit, stderr
import json


if len(argv) != 3:
    print("Usage: %s input_file output_file" % argv[0], file=stderr)
    exit(1)

task_input = open(argv[1], "r")
human_output = open(argv[2], "r")

# reading input file and generating correct output
T = int(task_input.readline())

outputs = []

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
	drones, nMoves, length = task_input.readline().strip().strip().split(" ")
	drones, nMoves, length = int(drones), int(nMoves), int(length)
	moves = []
	moves.append([ -1 for _ in range(length) ])
	hMoves = [ [] for _ in range(drones + 1) ]
	for i in range(1, nMoves + 1):
		p = []
		p = [ int(x) for x in task_input.readline().strip().strip().split(" ") ]
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
			outputs.append(s[0])
			return
		for m in hMoves[s[1]]:
			if (seen[m]): continue;
			dist = distance(s[2], m);
			if (dist >= 0):
				q.add((s[0] + dist, s[1] + 1, m));
	outputs.append(-1)

for i in range(T):
    task_input.readline().strip()
    test()

def evaluate(num, stream):
    correct_output = outputs[num-1]
    output = stream.int()

    if output == correct_output:
        return 1.0
    else:
        return 0.0


parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False, str_max_len=10**7)

print(json.dumps(parser.run()))