#!/usr/bin/env python3

# Checker Task 3: Calendario accademico
# Lorenzo Organtini | Mattia Cervellini
# need to tune parameters in the parser call


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

outputs = []

#!/usr/bin/env python3

def maxStud(stud, n, k):
    if 2*k >= n:
        maximprep = 0
        for i in range(1, n):
            if stud[i] > stud[i - 1]:
                maximprep += stud[i] - stud[i - 1]
        return maximprep

    impreparati = [[0 for i in range(n + 1)] for j in range(k + 1)]

    for i in range(1, k + 1):
        prevDiff = float('-inf')

        for j in range(1, n):
            prevDiff = max(prevDiff, impreparati[i - 1][j - 1] - stud[j - 1])
            impreparati[i][j] = max(impreparati[i][j - 1], stud[j] + prevDiff)

    return impreparati[k][n - 1]



ncasi = int(task_input.readline())
for caso in range(ncasi):
    task_input.readline()
    firstline = task_input.readline()
    n, k = firstline.strip().split(" ")
    n = int(n)
    k = int(k)
    stringprices = task_input.readline()
    prices = [int(x) for x in stringprices.strip().split(" ")]
    res = maxStud(prices, n, k)
    outputs.append(res)




def evaluate(num, stream):
    correct_output = outputs[num-1]
    output = stream.str()
    try:
        output = int(output)
    except ValueError:
        pass

    if output == correct_output:
        return 1.0
    else:
        return 0.0


parser = Parser(evaluate, ncasi, human_output, int_max_len=20, strict_spaces=False, str_max_len=10**7)

print(json.dumps(parser.run()))