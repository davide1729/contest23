#!/usr/bin/env python3

# Generator Task 4: Droni mutanti
# Lorenzo Organtini & Michele Lizzit

import random

# Limits
MAXN = 10**3 - 1
MAXM = 10**4
MAXT = 100
MAXT = 10

def genTc(forceK=None, maxN=MAXN, maxM=MAXM):
    assert maxM > maxN
    N = random.randint(2, maxN) if maxN > 2 else 2
    M = random.randint(1 + N, maxM) if maxM != 1 + N else maxM
    k = random.randint(4, 10) if forceK is None else forceK

    ensureValidCase = random.randint(1, 100) > 4
    seqPerDrone = int((M - N) / N) if ensureValidCase else int(M / N)

    # For each drone (last element) store the list of sequences that can deactivate it
    drones = [ [] for _ in range(N) ]

    for i in range(len(drones)):
        for _ in range( seqPerDrone ):
            if random.randint(1, 100) > 5: # Generage garbage sequence in 5% of sequences
                drones[i].append([ random.randint(0, N - 1) for j in range(k-1) ])
            else: # Ensure that the sequence is valid at least in the best case scenario
                drones[i].append([ random.randint(max( 0, i - ( k - 1 ) + j ), N - 1) for j in range(k-1) ])
        if ensureValidCase: # In 98% of cases add a sequence that is guaranteed to work ( take down only following drones )
            drones[i].append([ random.randint(i, N - 1) for _ in range(k-1) ])

    # Convert to the output case format
    finalSequences = []
    for i in range(len(drones)):
        finalSequences.extend( [ x + [i] for x in drones[i] ] )
    random.shuffle(finalSequences)
    assert len(finalSequences) <= M
    M = len(finalSequences)

    # Output test case
    print()
    print(f"{N} {M} {k}")
    for s in finalSequences:
        assert len(s) == k
        print(" ".join([ str(x) for x in s ]))


print(100)

genTc(forceK = 2, maxM = 60, maxN = 30)
for _ in range(24):
    genTc(forceK = 2, maxM = 10**3, maxN = 300)
for _ in range(25):
    genTc(forceK = 3, maxM = 10**3, maxN = 300)
for _ in range(25):
    genTc(forceK = 3)
for _ in range(25):
    genTc()