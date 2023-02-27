#!/usr/bin/env python3
# Lorenzo Organtini | Mattia Cervellini

def maxStud(stud, n, k):
    maximprep = 0
    for i in range(1, n):
        if stud[i] > stud[i - 1]:
            maximprep += stud[i] - stud[i - 1]
    return maximprep

ncasi = int(input())
for caso in range(ncasi):
    input()
    firstline = input()
    n, k = firstline.strip().split(" ")
    n = int(n)
    k = int(k)
    stringprices = input()
    prices = [int(x) for x in stringprices.strip().split(" ")]
    res = maxStud(prices, n, k)
    print(f"Case #{caso + 1}: {res}")