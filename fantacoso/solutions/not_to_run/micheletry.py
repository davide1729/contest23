#!/usr/bin/env python3

def knapsack(students, n, m, p):
    # initialize the dp array
    dp = [[[-1 for _ in range(101)] for _ in range(m*n+1)] for _ in range(n+1)]

    # fill in the dp array
    for j in range(m*n+1):
        dp[0][j][0] = 0
    for i in range(1, n+1):
        # get the attributes of the i-th student
        points, experience, gender = students[i-1]
        for j in range(experience, m*n+1):
            for k in range(gender, 101):
                if dp[i-1][j-experience][k-gender] != -1:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-experience][k-gender] + points)
                else:
                    dp[i][j][k] = dp[i-1][j][k]

    # find the optimal solution
    max_point = 0
    best_team = []
    for j in range(m*n, m*n-n, -1):
        for k in range(100, -1, -1):
            # check if the current gender balance is within the acceptable range
            if k*100/n <= p and k*100/n >= 100-p and dp[n][j][k] > max_point:
                max_point = dp[n][j][k]
                best_team = []

                # backtrack to find the students in the optimal team
                i = n
                remaining_exp = j
                remaining_gender = k
                while i > 0 and remaining_exp > 0 and remaining_gender >= 0:
                    if dp[i][remaining_exp][remaining_gender] == dp[i-1][remaining_exp][remaining_gender]:
                        # the i-th student was not selected, move to the previous student
                        i -= 1
                    else:
                        # the i-th student was selected, add them to the best team
                        best_team.append(students[i-1])
                        remaining_exp -= students[i-1][1]
                        remaining_gender -= students[i-1][2]
                        i -= 1
                if len(best_team) == n:
                    # we have found a team of n students with the maximum total points and acceptable gender balance, return it
                    return best_team[::-1]

    # if we reach here, we were unable to find a team of n students with the desired attributes, return the best team we have found so far
    return best_team[::-1]






students2=[(100,4,0),(90,4,1),(50,1,0),(45,2,1),(40,1,1)]
n2=1
m2=1
p2=70

"""
students1=[(160,4,1),(85,1,1),(90,2,1),(70,4,0)]
n1=2
m1=4
p1=90
"""

"print(knapsack(students1, n1, m1, p1))"

print(knapsack(students2, n2, m2, p2))