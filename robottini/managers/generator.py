#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 4 "Robottini Mercenari"
# INPUT GENERATOR
# Davide Beltrame
#####

import random

# Constraints

max_N = 10
easy_N = int(max_N/5)
avg_N = int(max_N/3)
int_N = int(max_N/2)
min_N = 1
max_M = 100
easy_M = int(max_M/5)
avg_M = int(max_M/3)
int_M = int(max_M/2)
min_M = 2
max_P = 1000


def easy_cases():
    
    N = random.randint(min_N, easy_N)
    M = random.randint(min_M, easy_M)
    print(N)
    print(M)
    models = random.choices(range(2,M+1), k=N)
    powers = [random.randint(0, max_P) for j in range(N)]
    print(" ".join(str(x) for x in models))
    print(" ".join(str(x) for x in powers))

def average_cases():
    
    N = random.randint(easy_N, avg_N)
    M = random.randint(easy_M, avg_M)
    print(N)
    print(M)
    models = random.choices(range(2,M+1), k=N)
    powers = [random.randint(0, max_P) for j in range(N)]
    print(" ".join(str(x) for x in models))
    print(" ".join(str(x) for x in powers))

def intermediate_cases():
    
    N = random.randint(avg_N, int_N)
    M = random.randint(avg_M, int_M)
    print(N)
    print(M)
    models = random.choices(range(2,M+1), k=N)
    powers = [random.randint(0, max_P) for j in range(N)]
    print(" ".join(str(x) for x in models))
    print(" ".join(str(x) for x in powers))

def advanced_cases():

    N = random.randint(min_N, max_N)
    M = random.randint(min_M, max_M)
    print(N)
    print(M)
    models = random.choices(range(2,M+1), k=N)
    powers = [random.randint(0, max_P) for j in range(N)]
    print(" ".join(str(x) for x in models))
    print(" ".join(str(x) for x in powers))

def edge_cases():
    
    N = 1
    M = 2
    print(N)
    print(M)
    models = random.choices(range(2,M+1), k=N)
    powers = [random.randint(0, max_P) for j in range(N)]
    print(" ".join(str(x) for x in models))
    print(" ".join(str(x) for x in powers))

CASES = [easy_cases]*4 + [average_cases]*4 + [intermediate_cases]*5 + [advanced_cases]*8 + [edge_cases]*4
print(len(CASES)) # DEVE PRINTARE 25

for x in CASES:
	print() # spazio vuoto
	x() # ogni caso di test