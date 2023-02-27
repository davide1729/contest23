#!/usr/bin/env python3

#
# Generator Final Contest LUISSMatics 2022
# Task n. 1 "Café Cypher (cifrario)"
# Demetrio Cardile, Davide Beltrame
#
import string
import random

MAXN = 100
Naverage = 30
Nintermed = 50
MAXK = 100
MAXC = MAXK
MAXk = 10**3
MAXc = MAXN

#Generator_contest

def easy_cases():
    chars_list = []
    keys_list = []

    #random_str creation
    N = random.randint(1,50)
    random_str = ''.join(random.choices(string.ascii_letters, k=N))

    #shifting_keys creation
    K = random.randint(1,MAXK)
    if K > len(random_str):
        K = len(random_str)
    if K == 0:
        keys_list.append(0)
        chars_list.append(0)

    for i in range(K):
        keys_list.append(random.randint(0,26))
    
    #number of chars to be shifted
    for i in range(K):
        chars_list.append(random.randint(0,len(random_str)))
    
    #structure of input_file
    print(N, K)
    print(random_str)
    print(*keys_list, sep=' ')
    print(*chars_list, sep=' ')

def average_cases():
    chars_list = []
    keys_list = []

    #random_str creation
    N = random.randint(1,Naverage)
    random_str = ''.join(random.choices(string.ascii_letters, k=N))

    #shifting_keys creation
    K = random.randint(1,MAXK)
    if K > len(random_str):
        K = len(random_str)
    if K == 0:
        keys_list.append(0)
        chars_list.append(0)

    for i in range(K):
        keys_list.append(random.randint(0,MAXk))
    
    #number of chars to be shifted
    for i in range(K):
        chars_list.append(random.randint(0,len(random_str)))
    
    #structure of input_file
    print(N, K)
    print(random_str)
    print(*keys_list, sep=' ')
    print(*chars_list, sep=' ')

def intermediate_cases():
    chars_list = []
    keys_list = []

    #random_str creation
    N = random.randint(1,Nintermed)
    random_str = ''.join(random.choices(string.ascii_letters, k=N))

    #shifting_keys creation
    K = random.randint(1,MAXK)
    if K > len(random_str):
        K = len(random_str)
    if K == 0:
        keys_list.append(0)
        chars_list.append(0)

    for i in range(K):
        keys_list.append(random.randint(0,MAXk))
    
    #number of chars to be shifted
    for i in range(K):
        chars_list.append(random.randint(0,len(random_str)))
    
    #structure of input_file
    print(N, K)
    print(random_str)
    print(*keys_list, sep=' ')
    print(*chars_list, sep=' ')

def advanced_cases():
    chars_list = []
    keys_list = []

    #random_str creation
    N = random.randint(1,MAXN)
    random_str = ''.join(random.choices(string.ascii_letters, k=N))

    #shifting_keys creation
    K = random.randint(1,MAXK)
    if K > len(random_str):
        K = len(random_str)
    if K == 0:
        keys_list.append(0)
        chars_list.append(0)

    for i in range(K):
        keys_list.append(random.randint(0,MAXk))
    
    #number of chars to be shifted
    for i in range(K):
        chars_list.append(random.randint(0,len(random_str)))
    
    #structure of input_file
    print(N, K)
    print(random_str)
    print(*keys_list, sep=' ')
    print(*chars_list, sep=' ')

def shift_keys_0_case():
    chars_list = []
    keys_list = []

    #random_str creation
    N = random.randint(1,10)
    random_str = ''.join(random.choices(string.ascii_letters, k=N))

    #shifting_keys creation
    K = random.randint(1,MAXK)
    if K > len(random_str):
        K = len(random_str)
    if K == 0:
        keys_list.append(0)
        chars_list.append(0)

    for i in range(K):
        keys_list.append(int(0))
    
    #number of chars to be shifted
    for i in range(K):
        chars_list.append(random.randint(0,len(random_str)))
    
    #structure of input_file
    print(N, K)
    print(random_str)
    print(*keys_list, sep=' ')
    print(*chars_list, sep=' ')

def chars_0_cases():
    chars_list = []
    keys_list = []

    #random_str creation
    N = random.randint(1,MAXN)
    random_str = ''.join(random.choices(string.ascii_letters, k=N))

    #shifting_keys creation
    K = random.randint(1,MAXK)
    if K > len(random_str):
        K = len(random_str)
    if K == 0:
        keys_list.append(0)
        chars_list.append(0)

    for i in range(K):
        keys_list.append(random.randint(0,MAXk))
    
    #number of chars to be shifted
    for i in range(K):
        chars_list.append(int(0))
    
    #structure of input_file
    print(N, K)
    print(random_str)
    print(*keys_list, sep=' ')
    print(*chars_list, sep=' ')

CASES = [easy_cases]*2 + [average_cases]*4 + [intermediate_cases]*4 + [advanced_cases]*8 + [shift_keys_0_case]*4 + [chars_0_cases]*3

print(len(CASES))

for x in CASES:
	print()
	x()
