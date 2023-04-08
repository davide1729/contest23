#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 1 "fantacoso"
# INPUT GENERATOR
# Michele Turco
#####

# import librerie
import random

# Constraint
MAXK = 5
MAXN = MAXK
MAXE = MAXK*5
MAXP = 100
MAX_experience=5
MIN_experience=1
MAX_point=200



def easy_cases():
    K=random.randint(1,MAXK)
    P=100
    E=100
    N=K
    print(K,N,E,P)
    for i in range(K):
         points = random.randint(0, 200)  # generate a random number between 0 and 100 for points
         experience = random.randint(1, 5)  # generate a random number for experience, not exceeding M
         gender = random.randint(0,1)  # generate a random number between 0 and 1 for gender
         # print the three numbers separated by spaces
         print(points, experience, gender)

def average_cases():
    K=random.randint(1,MAXK)
    P=random.randint(0,100)
    E=random.randint(1,K*5)
    N=random.randint(20,K)
    print(K,N,E,P)
    for i in range(K):
         points = random.randint(0, 200)  # generate a random number between 0 and 100 for points
         experience = random.randint(1, 5)  # generate a random number for experience, not exceeding M
         gender = random.randint(0,1)  # generate a random number between 0 and 1 for gender
         # print the three numbers separated by spaces
         print(points, experience, gender)
            
def intermediate_cases():
    K=random.randint(1,MAXK)
    P=random.randint(0,100)
    E=random.randint(1,K*5)
    N=random.randint(1,K)
    print(K,N,E,P)
    for i in range(K):
         points = random.randint(0, 200)  # generate a random number between 0 and 100 for points
         experience = random.randint(1, 5)  # generate a random number for experience, not exceeding M
         gender = random.randint(0,1)  # generate a random number between 0 and 1 for gender
         # print the three numbers separated by spaces
         print(points, experience, gender)

def advanced_cases():
    K=random.randint(1,MAXK)
    P=random.randint(0,100)
    E=random.randint(1,K*5)
    N=random.randint(1,K)
    print(K,N,E,P)
    for i in range(K):
         points = random.randint(0, 200)  # generate a random number between 0 and 100 for points
         experience = random.randint(1, 5)  # generate a random number for experience, not exceeding M
         gender = random.randint(0,1)  # generate a random number between 0 and 1 for gender
         # print the three numbers separated by spaces
         print(points, experience, gender)

def edge_cases():
    K=random.randint(1,MAXK)
    P=0
    E=random.randint(1,K*5)
    N=random.randint(1,K)
    print(K,N,E,P)
    for i in range(K):
         points = random.randint(0, 200)  # generate a random number between 0 and 100 for points
         experience = random.randint(1, 5)  # generate a random number for experience, not exceeding M
         gender = random.randint(0,1)  # generate a random number between 0 and 1 for gender
         # print the three numbers separated by spaces
         print(points, experience, gender)

CASES = [easy_cases]*2 + [average_cases]*7 + [intermediate_cases]*7 + [advanced_cases]*8 + [edge_cases]*1

print(len(CASES)) 
for x in CASES:
     print()
     x()
