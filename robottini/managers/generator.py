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
min_N = 1
max_M = 100
min_M = 2
max_P = 100


def easy_cases():
    
    N = random.randint(min_N, max_N)
    M = random.randint(min_M, max_M)
    print(N)
    print(M)
    models = random.choices(range(2,M+1), k=N)
    powers = [random.randint(0, max_P) for j in range(N)]
    print(" ".join(str(x) for x in models))
    print(" ".join(str(x) for x in powers))

def average_cases():
    
    #structure of input_file
    print(N, K)

def intermediate_cases():
    
    #structure of input_file
    print(N, K)

def advanced_cases():

    #structure of input_file
    print(N, K)

def shift_keys_0_case():
    
    #structure of input_file
    print(N, K)

def chars_0_cases():

    #structure of input_file
    print(N, K)

CASES = [easy_cases]*25 + [average_cases]*4 + [intermediate_cases]*4 + [advanced_cases]*8 + [shift_keys_0_case]*4 + [chars_0_cases]*3
CASES = [easy_cases]*25
print(len(CASES)) # DEVE PRINTARE 25

for x in CASES:
	print() # spazio vuoto
	x() # ogni caso di test