#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. x "fantacoso"
# INPUT GENERATOR
# Michele Turco
#####

# import librerie
import random

# Constraint
MAXK = 5*10**2
MAXN = MAXK
MAXM = 25*10**2
MAXP = 100
MAX_experience=5
MIN_experience=1
MAX_point=200



def easy_cases():
    K=random.randint(10,20)
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
    K=random.randint(70,100)
    P=random.randint(0,100)
    E=random.randint(40,400)
    N=random.randint(20,K)
    print(K,N,E,P)
    for i in range(K):
         points = random.randint(0, 200)  # generate a random number between 0 and 100 for points
         experience = random.randint(1, 5)  # generate a random number for experience, not exceeding M
         gender = random.randint(0,1)  # generate a random number between 0 and 1 for gender
         # print the three numbers separated by spaces
         print(points, experience, gender)
            
def intermediate_cases():
    K=random.randint(150,250)
    P=random.randint(0,100)
    E=random.randint(100,1000)
    N=random.randint(60,K)
    print(K,N,E,P)
    for i in range(K):
         points = random.randint(0, 200)  # generate a random number between 0 and 100 for points
         experience = random.randint(1, 5)  # generate a random number for experience, not exceeding M
         gender = random.randint(0,1)  # generate a random number between 0 and 1 for gender
         # print the three numbers separated by spaces
         print(points, experience, gender)

def advanced_cases():
    K=random.randint(300,500)
    P=random.randint(0,100)
    E=random.randint(1001,2000)
    N=random.randint(200,K)
    print(K,N,E,P)
    for i in range(K):
         points = random.randint(0, 200)  # generate a random number between 0 and 100 for points
         experience = random.randint(1, 5)  # generate a random number for experience, not exceeding M
         gender = random.randint(0,1)  # generate a random number between 0 and 1 for gender
         # print the three numbers separated by spaces
         print(points, experience, gender)

def edge_cases():
    K=random.randint(10,20)
    P=0
    N=random.randint(5,K)
    E=random.randint(20,80)
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
