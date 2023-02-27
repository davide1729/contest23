#!/usr/bin/env python3
# Lorenzo Organtini | Mattia Cervellini

ncasi = int(input())
for caso in range(ncasi):
    input()
    firstline = input()
    n, k = firstline.strip().split(" ")
    n = int(n)
    k = int(k)
    stringprices = input()
    prices = [int(x) for x in stringprices.strip().split(" ")]
    res = prices[-1] - prices[0]
    print(f"Case #{caso + 1}: {res}")