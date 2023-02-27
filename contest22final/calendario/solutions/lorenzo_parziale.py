#!/usr/bin/env python3
# Lorenzo Organtini

def maxStud(stud, n, k):
    impreparati = [[0 for i in range(n + 1)] for j in range(k + 1)]

    for i in range(1, k + 1):
        prevDiff = float('-inf')

        for j in range(1, n):
            prevDiff = max(prevDiff, impreparati[i - 1][j - 1] - stud[j - 1])
            impreparati[i][j] = max(impreparati[i][j - 1], stud[j] + prevDiff)

    return impreparati[k][n - 1]

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
    print(f"case #{caso + 1}: {res}")

