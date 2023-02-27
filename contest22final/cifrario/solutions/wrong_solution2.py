#!/usr/bin/env python3
# Davide Beltrame, Demetrio Cardile

import string

def cipher2(str,k1,k2,k3,c1,c2,c3):
    letters = string.ascii_letters
    final_str = ''
    rep_counter = 0
    counter = 0
    for letter in str:
        for j in range(len(letters)-1):
            if letter == '':
                final_str += ''
                counter += 1
                rep_counter += 1
            if letter == letters[j]:
                counter = 0
                while counter <= c1:
                    final_str += letters[j+k1]
                    counter += 1
                    rep_counter += 1
                counter = 0
                while counter <= c2:
                    final_str += letters[j+k2]
                    counter += 1
                    rep_counter += 1
                counter = 0
                while counter <= c3:
                    final_str += letters[j+k3]
                    counter += 1
                    rep_counter += 1
    return final_str
#print(cipher2('abcde', 0, 1, 2, 1, 1, 2))

T = int(input())

for t in range(T):
    input()
    N, K = input().strip().split(" ")
    text = str(input())
    if K != '0':
        keys = input().strip().split(" ")
        chars = input().strip().split(" ")
        for i in keys:
            k1 = int(keys[0])
            k2 = int(keys[1])
            k3 = int(keys[2])
        for i in chars:
            c1 = int(chars[0])
            c2 = int(chars[1])
            c3 = int(chars[2])
        print('Case #'+str(t+1)+': '+str(cipher2(text,k1,k2,k3,c1,c2,c3)))
    else:
        print('Case #'+str(t+1)+': ',text)