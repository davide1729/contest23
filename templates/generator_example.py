#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. x "Nome Task"
# INPUT GENERATOR
# Autori
#####

# import librerie
import random

# Constraint
MAXN = 100
Naverage = 30
Nintermed = 50
MAXK = 100
MAXC = MAXK
MAXk = 10**3
MAXc = MAXN

def easy_cases():
    
    #structure of input_file
    print(N, K)
    print(random_str)
    print(*keys_list, sep=' ')
    print(*chars_list, sep=' ')

def average_cases():
    
    #structure of input_file
    print(N, K)
    print(random_str)
    print(*keys_list, sep=' ')
    print(*chars_list, sep=' ')

def intermediate_cases():
    
    #structure of input_file
    print(N, K)
    print(random_str)
    print(*keys_list, sep=' ')
    print(*chars_list, sep=' ')

def advanced_cases():

    #structure of input_file
    print(N, K)
    print(random_str)
    print(*keys_list, sep=' ')
    print(*chars_list, sep=' ')

def shift_keys_0_case():
    
    #structure of input_file
    print(N, K)
    print(random_str)
    print(*keys_list, sep=' ')
    print(*chars_list, sep=' ')

def chars_0_cases():

    #structure of input_file
    print(N, K)
    print(random_str)
    print(*keys_list, sep=' ')
    print(*chars_list, sep=' ')

CASES = [easy_cases]*2 + [average_cases]*4 + [intermediate_cases]*4 + [advanced_cases]*8 + [shift_keys_0_case]*4 + [chars_0_cases]*3

print(len(CASES)) # DEVE PRINTARE 25

for x in CASES:
	print() # spazio vuoto
	x() # ogni caso di test