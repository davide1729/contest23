#!/usr/bin/env python3

#
# BOZZA Checker Final Contest LUISSMatics 2022
# Task n. 1 "Café Cypher (cifrario)"
# Demetrio Cardile, Davide Beltrame
#

from distutils.command.build_scripts import first_line_re
import string
from functools import lru_cache
from itertools import accumulate
from parser import Parser
import json
from sys import argv, exit, stderr

if len(argv) != 3:
    print("Usage: %s input_file output_file" % argv[0], file=stderr)
    exit(1)

task_input = open(argv[1], "r")
human_output = open(argv[2], "r")

# reading input file and generating correct output

outputs = [] 

def shift(char, s):
	if (char.isupper()):
		result = chr((ord(char) + s - 65) % 26 + 65)
	else:
		result = chr((ord(char) + s - 97) % 26 + 97)
	return result

T = int(task_input.readline())

for t in range(T):
	task_input.readline()
	numchars, numkeys = [ int(x) for x in task_input.readline().strip().split(" ") ]
	s = task_input.readline().strip()
	keys = [ int(x) for x in task_input.readline().strip().split(" ") ]
	keylen = [ int(x) for x in task_input.readline().strip().split(" ") ]
	finalkeys = []
	for k, l in zip(keys, keylen):
		finalkeys += [k] * l
	if len(finalkeys) == 0:
		outputs.append(s)
		continue
	while len(finalkeys) <= len(s):
		finalkeys *= 2

	res = ""
	for c,i in zip(s, range(len(s))):
		res += shift(c, finalkeys[i])
	outputs.append(res)

def evaluate(num, stream):
    correct_output = outputs[num-1]
    user_output = stream.str()
    stream.end()
    if user_output == correct_output:
        return 1.0
    else:
        return 0.0

parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False)

print(json.dumps(parser.run()))

#checker old version (working)

'''
#!/usr/bin/env python3

#
# BOZZA Checker Final Contest LUISSMatics 2022
# Task n. 1 "Café Cypher (cifrario)"
# Demetrio Cardile, Davide Beltrame
#

from distutils.command.build_scripts import first_line_re
import string
from functools import lru_cache
from itertools import accumulate
from parser import Parser
import json
from sys import argv, exit, stderr

if len(argv) != 3:
    print("Usage: %s input_file output_file" % argv[0], file=stderr)
    exit(1)

task_input = open(argv[1], "r")
human_output = open(argv[2], "r")

# reading input file and generating correct output

outputs = [] 

def shift(char, s):
	if (char.isupper()):
		result = chr((ord(char) + s - 65) % 26 + 65)
	else:
		result = chr((ord(char) + s - 97) % 26 + 97)
	return result

T = int(task_input.readline())

for t in range(T):
	task_input.readline()
	numchars, numkeys = [ int(x) for x in task_input.readline().strip().split(" ") ]
	s = task_input.readline().strip()
	keys = [ int(x) for x in task_input.readline().strip().split(" ") ]
	keylen = [ int(x) for x in task_input.readline().strip().split(" ") ]
	finalkeys = []
	for k, l in zip(keys, keylen):
		finalkeys += [k] * l
	if len(finalkeys) == 0:
		outputs.append(s)
		continue
	while len(finalkeys) <= len(s):
		finalkeys *= 2

	res = ""
	for c,i in zip(s, range(len(s))):
		res += shift(c, finalkeys[i])
	outputs.append(res)

def evaluate(num, stream):
    correct_output = outputs[num-1]
    user_output = stream.str()
    stream.end()
    if user_output == correct_output:
        return 1.0
    else:
        return 0.0

parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False)

print(json.dumps(parser.run()))
'''