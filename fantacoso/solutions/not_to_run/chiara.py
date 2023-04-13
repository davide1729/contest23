#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 1 "FantaOlimpiadi"
# Tentative SOLUTION
# Chiara Baldoni
#####

from itertools import combinations

def select_team(candidates, N, E, B):
    maxP = 0

    for team in combinations(candidates,N):
        sumMALE = 0
        sumP = 0
        sumE = 0
        for c in team:
            sumE += c[1]
            if c[2] == 1:
                sumMALE +=1
            sumP += c[0]
        # checks
        if sumE <= E:
            continue
        if sumMALE <= B:
            continue

        # team is legit
        if sumP > maxP:
            maxP = sumP
          
    return maxP


T=int(input())

for t in range(1,T+1):
    input()
    ln=input().split(" ")
    K=int(ln[0]) #number of students in the school
    N=int(ln[1]) #maximum number of students that can be selected for a team
    E=int(ln[2]) #maximum experience
    B=int(ln[3]) #maximum percentage of boys

    experiences=[0] #list with the experiences for boys and girls
    boys=[0] #list with the gender (1 for male, 0 for female)
    points=[0] #list with the scores 
    students=[[],[],[]]
    
    for i in range(K):
        ln=input().split()
        students[0].append(int(ln[0]))
        students[1].append(int(ln[1]))
        students[2].append(int(ln[2]))
    res=select_team(students,N,E,B)

    print(f"Case #{t}: {res}")