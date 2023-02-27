#!/usr/bin/env python3

#
# Generator Final Contest LUISSMatics 2022
# Task n. 2 "Orientamento"
# Maria Chiara Lischi, Matteo Spadaccia
#

import random

#Generator_contest

def easy_case():
    N = random.randint(10**2, 10**3)
    P = random.randint(10**2, 10**3)
    a = random.randint(1, 10**2)
    x = random.randint(2, 10**2)
    return N, P, a, x

def average_case():
    N = random.randint(10**5, 10**6)
    P = random.randint(10**3, 10**4)
    a = random.randint(1, 10**2)
    x = random.randint(2, 10**2)
    return N, P, a, x

def intermediate_case():
    N = random.randint(10**8, 10**9)
    P = random.randint(10**4, 10**5)
    a = random.randint(1, 10**2)
    x = random.randint(2, 10**2)
    return N, P, a, x

def advanced_case():
    N = random.randint (10**10, 10**11)
    P = random.randint(10**5, 10**6)
    a = random.randint(1, 10**2)
    x = random.randint(2, 10**2)
    return N, P, a, x

def edge_case1():
    N = 1
    P = random.randint(10**3, 10**4)
    a = random.randint(1, 10**2)
    x = random.randint(2, 10**2)
    return N, P, a, x
    
def edge_case2():
    N = random.randint(10**5, 10**6)
    P = 2
    a = 1
    x = random.randint(2, 10**2)
    return N, P, a, x
    
def edge_case3():
    N = random.randint(10**5, 10**6)
    P = random.randint(10**3, 10**4)
    a = random.randint(1, 10**2)
    x = 2
    return N, P, a, x
    
def edge_case4():
    N = random.randint(10**5, 10**6)
    P = random.randint(10**3, 10**4)
    a = random.randint(1, 10**2)
    x = 10**2
    return N, P, a, x
    
def edge_case5():
    N = random.randint(10**5, 10**6)
    P = random.randint(10**3, 10**4)
    a = P
    x = random.randint(2, 10**2)
    return N, P, a, x       
    
def inputfile():
    inp = ""
    for i in range(10):
        tup = easy_case()
        inp += "\n" + str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + " " + str(tup[3]) + "\n"
        
    for i in range(10):
        tup = average_case()
        inp += "\n" + str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + " " + str(tup[3]) + "\n"
        
    for i in range(10):
        tup = intermediate_case()
        inp += "\n" + str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + " " + str(tup[3]) + "\n"
        
    for i in range(10):
        tup = advanced_case()
        inp += "\n" + str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + " " + str(tup[3]) + "\n"
        
    for i in range(2):
        tup = edge_case1()
        inp += "\n" + str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + " " + str(tup[3]) + "\n"
        
    for i in range(2):
        tup = edge_case2()
        inp += "\n" + str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + " " + str(tup[3]) + "\n"
        
    for i in range(2):
        tup = edge_case3()
        inp += "\n" + str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + " " + str(tup[3]) + "\n"
        
    for i in range(2):
        tup = edge_case4()
        inp += "\n" + str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + " " + str(tup[3]) + "\n"
        
    for i in range(2):
        tup = edge_case5()
        inp += "\n" + str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + " " + str(tup[3]) + "\n"
      
    return inp

input_str = inputfile()
print(input_str)