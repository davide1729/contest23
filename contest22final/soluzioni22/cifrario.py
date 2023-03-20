#!/usr/bin/env python3
# Davide Beltrame, Demetrio Cardile

import string
from functools import lru_cache

"""with open("input.txt","r") as input:
    input2 = input.readlines()
    input3 = []
    for line in input2:
        input3.append(line.split('\n')[0])
    for i in range(len(input3)):
        if ' ' in input3[i]:
            input3[i] = input3[i].split(' ')"""

def encryption_3(text,keys,chars):
    sum = 0
    sum2 = 0
    final_str = shifter(text)
    for i in chars:
        sum += int(i)
    if sum < len(text):
        while True:
            sum2 += sum
            rest = text[sum2:]
            shifter(rest)
            final_str += temp_str
            if len(final_str)>=len(text):
                final_str = final_str[:len(text)]
                break  
            elif len(final_str) == 0:
                final_str = text
                break
    return final_str

@lru_cache()
def shifter(text):
    t = 0
    j = 0
    global temp_str
    temp_str = ''
    shifted = ''
    for i in range(len(keys)): 
        if int(chars[i]) != 0:
            if i > 0:
                t += int(chars[i-1])
            j += int(chars[i])
            shiftandum = text[t:j]
            shifted = caesarCipher2(shiftandum, int(keys[i]))
            temp_str += shifted
    return temp_str

@lru_cache()
def caesarCipher2(str, n):
    b = 2*(string.ascii_lowercase) # this
    c = 2*(string.ascii_uppercase) # and this ensure cases conservation (a!=A)
    n = n%26 # this prevents out-of-range error
    temp_str = ''
    for i in str:
        if i == ' ': # this
            temp_str += ' ' # and this ensure blank spaces conservation
        for j in range(len(b)//2): # the range is a normal alphabet, half of b
            if i == b[j]:
                temp_str += b[j+n]
            elif i == c[j]:
                temp_str += c[j+n]
    return temp_str

T = int(input())
keys_backup = []
chars_backup = []
solved = []

for i in range(T):
    input()
    N, K = input().strip().split(" ")
    text = str(input())
    if K != '0':
        keys = input().strip().split(" ")
        chars = input().strip().split(" ")
        if keys == str(keys):
            keys_backup.append(keys)
            keys = keys_backup
        if chars == str(chars):
            chars_backup.append(chars)
            chars = chars_backup
        solved.append('Case #'+str(i+1)+': '+encryption_3(text,keys,chars))
    else:
        solved.append('Case #'+str(i+1)+': '+text)

for i in range(T):
    print(solved[i])