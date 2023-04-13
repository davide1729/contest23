#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 1 "FantaOlimpiadi"
# SOLUTION CHECKER
# Michele Turco, Chiara Baldoni
#####

from distutils.command.build_scripts import first_line_re
# import librerie necessarie
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

def knapsack(genders, experiences, scores, max_gender_ratio, max_experience, max_student):
    n = len(genders)
    dp = [[[(0, []) for _ in range(max_gender_ratio+1)] for _ in range(max_experience+1)] for _ in range(max_student+1)]
    
    for i in range(1, n+1):
        for j in range(max_student, 0, -1):
            for k in range(max_experience, -1, -1):
                for l in range(max_gender_ratio, -1, -1):
                    if j == 1:
                        if genders[i-1] <= l and experiences[i-1] <= k:
                            if dp[j][k][l][0] < scores[i-1]:
                                dp[j][k][l] = (scores[i-1], [i-1])
                    else:
                        if genders[i-1] <= l and experiences[i-1] <= k:
                            if dp[j][k][l][0] < dp[j-1][k-experiences[i-1]][l-genders[i-1]][0] + scores[i-1]:
                                dp[j][k][l] = (dp[j-1][k-experiences[i-1]][l-genders[i-1]][0] + scores[i-1], dp[j-1][k-experiences[i-1]][l-genders[i-1]][1] + [i-1])
    
    return dp[max_student][max_experience][max_gender_ratio]

T = int(task_input.readline())

for t in range(1,T+1):
    task_input.readline()
	# mettere soluzione in res
    ln=task_input.readline().split(" ")
    K=int(ln[0]) #number of students in the school
    N=int(ln[1]) #maximum number of students that can be selected for a team
    E=int(ln[2]) #maximum experience
    B=int(ln[3]) #maximum number of boys

    experiences=[0] #list with the experiences for boys and girls
    boys=[0] #list with the gender (1 for male, 0 for female)
    points=[0] #list with the scores 
    
    for i in range(K):
        ln=task_input.readline().split()
        points.append(int(ln[0]))
        experiences.append(int(ln[1]))
        boys.append(int(ln[2]))
    res=knapsack(boys,experiences,points,B,E,N)[0]

    outputs.append(str(res))

def evaluate(num, stream):
    correct_output = outputs[num-1] # quelli del checker
    user_output = stream.str() # quello della soluzione
    stream.end()
    if user_output == correct_output:
        return 1.0
    else:
        return 0.0

parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False)

print(json.dumps(parser.run()))