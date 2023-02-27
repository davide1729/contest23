#!/usr/bin/env python3
# Davide Beltrame, Demetrio Cardile

import string

def cypher(text,k1,k2,k3,c1,c2,c3):
    alphabet = string.ascii_letters
    final_str = ''
    len_counter = 0

    if len(text) == 0:
        return 

    text1 = text[:c1]
    #print(text1)
    shifted1 = alphabet[k1:] + alphabet[:k1]
    table1 = str.maketrans(alphabet, shifted1)
    encr1 = text1.translate(table1)
    final_str += encr1
    len_counter += len(text1)

    text2 = text[c1:c1+c2]
    #print(text2)
    shifted2 = alphabet[k2:] + alphabet[:k2]
    table2 = str.maketrans(alphabet, shifted2)
    encr2 = text2.translate(table2)
    final_str += encr2
    len_counter += len(text2)

    text3 = text[c1+c2:c1+c2+c3]
    #print(text3)
    shifted3 = alphabet[k3:] + alphabet[:k3]
    table3 = str.maketrans(alphabet, shifted3)
    encr3 = text3.translate(table3)
    final_str += encr3
    len_counter += len(text3)
    
    if len_counter <= len(text):
        cypher(text[c1+c2+c3:],k1,k2,k3,c1,c2,c3)
    
    return final_str
#print(cypher('abcde',0,2,1,1,1,2))

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
        print('Case #'+str(t+1)+': '+str(cypher(text,k1,k2,k3,c1,c2,c3)))
    else:
        print('Case #'+str(t+1)+': ',text)