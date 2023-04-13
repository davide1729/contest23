#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 1 "FantaOlimpiadi"
# CORRECT SOLUTION
# Michele Turco
#####

"""
@author: Michele Turco

Task: fantacoso
"""
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

T=int(input())

for t in range(1,T+1):
    input()
    ln=input().split(" ")
    K=int(ln[0]) #number of students in the school
    N=int(ln[1]) #maximum number of students that can be selected for a team
    E=int(ln[2]) #maximum experience
    P=int(ln[3]) #maximum percentage of boys

    experiences=[0] #list with the experiences for boys and girls
    boys=[0] #list with the gender (1 for male, 0 for female)
    points=[0] #list with the scores 
    
    for i in range(K):
        ln=input().split()
        points.append(int(ln[0]))
        experiences.append(int(ln[1]))
        boys.append(int(ln[2]))
    res=knapsack(boys,experiences,points,P,E,N)[0]

    print(f"Case #{t}: {res}")






