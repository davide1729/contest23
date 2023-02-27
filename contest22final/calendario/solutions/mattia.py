#!/usr/bin/env python3
# Mattia Cervellini

ncases = int(input())
for case in range(ncases):
    input()
    firstline = input()
    n, k = firstline.strip().split(" ")
    n = int(n)
    k = int(k)
    stringprices = input()
    prenotazioni = [int(x) for x in stringprices.strip().split(" ")]

    if k == 0 or n <= 1:
        maximprep = 0
    elif 2*k >= n:
        maximprep = 0
        for i in range(1, n):
            if prenotazioni[i] > prenotazioni[i - 1]:
                maximprep += prenotazioni[i] - prenotazioni[i - 1]
    else:
        dp = [0]*(2*k)
        for idx in range(len(dp)):
            if idx % 2 == 0:
                dp[idx] = -10**12
            else:
                dp[idx] = 0

        for i in range(len(prenotazioni)):
            for j in range(len(dp)):
                if j == 0:
                    dp[j] = max(dp[j], -prenotazioni[i])
                elif j % 2 == 0:
                    dp[j] = max(dp[j], dp[j-1] - prenotazioni[i])
                else:
                    dp[j] = max(dp[j], dp[j-1] + prenotazioni[i])
        maximprep = dp[-1]
    print(f"Case #{case + 1}: {maximprep}")