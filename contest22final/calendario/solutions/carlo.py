#!/usr/bin/env python3
#Carlo Malagnino

import math

def maxProfit(k, prices) -> int:
    n = len(prices)

    if not prices or k==0:
        return 0

    if 2*k > n:
        res = 0
        for i, j in zip(prices[1:], prices[:-1]):
            res += max(0, i - j)
        return res

    dp = [[[-math.inf]*2 for _ in range(k+1)] for _ in range(n)]

    dp[0][0][0] = 0
    dp[0][1][1] = -prices[0]
    
    for i in range(1, n):
        for j in range(k+1):
            
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
            
            if j > 0:
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

    res = max(dp[n-1][j][0] for j in range(k+1))
    return res

ncasi = int(input())
for caso in range(ncasi):
    input()
    firstline = input()
    n, k = firstline.strip().split(" ")
    n = int(n)
    k = int(k)
    stringprices = input()
    prices = [int(x) for x in stringprices.strip().split(" ")]
    res = maxProfit(k, prices)
    print(f"Case #{caso + 1}: {res}")
