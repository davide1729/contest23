from itertools import combinations

NAME = 0
P = 1
E = 2
G = 3
MALE = 1



def select_team(candidates, K, M, PERC):
    maxP = 0
    best_teams = []

    for team in combinations(candidates,K):
        # stats
        sumMALE = 0
        sumP = 0
        sumE = 0
        for c in team:
            sumE += c[E]
            if c[G] == MALE:
                sumMALE +=1
            sumP += c[P]
        # checks
        if sumE != M * K:
            continue
        if sumMALE * 100 > PERC * K:
            continue
        if (K-sumMALE) * 100 > PERC * K:
            continue

        # team is legit
        if sumP > maxP:
            maxP = sumP
            best_teams = [team]
            #print("new max", maxP, best_teams)
        elif sumP == maxP:
            best_teams.append(team)
            #rint("ex equo", maxP, best_teams)
    
    assert len(best_teams) == 1
    return best_teams[0]


def print_team(case, team):
    from operator import itemgetter
    players = sorted(team, key=itemgetter(1), reverse=True)
    print(f"Case#{case}:", end="")
    for c in players:
        print(f" {c[NAME]}", end="")
    print()






tests = [
    {
        'N': 4,
        'K': 2,
        'M': 4,
        'PERC': 60,
        'candidates': [
            [1, 160, 4, 1],
            [2, 85, 1, 1], 
            [3, 90, 2, 1], 
            [4, 70, 4, 2]
        ]
    },
    {
        'N': 5,
        'K': 3,
        'M': 3,
        'PERC': 70,
        'candidates': [
            [1, 45, 2, 1],
            [2, 40, 1, 1], 
            [3, 50, 1, 2], 
            [4, 90, 4, 1],
            [5, 100, 4, 2],
        ]
    }
]

for case, test in enumerate(tests):
    N = test['N']
    K = test['K']
    M = test['M']
    PERC = test['PERC']
    candidates = test['candidates']
    assert len(candidates) == N
    print_team(case+1, select_team(candidates, K, M, PERC))