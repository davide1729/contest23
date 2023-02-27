#!/usr/bin/env python3

# Generator Task 4: Droni mutanti
# Lorenzo Organtini

import random

def first(T, Cf, Cs):
    k = 2

    for t in range(T): # casi random
        N = random.randint(2, 100)
        M = random.randint(N, 5000)
        print(str(N) + ' ' + str(M) + ' ' + str(k))

        for m in range(M):
            sequence = [str(random.randint(0,N-1)) for pos in range(k)]
            print(' '.join(sequence))
        print()

    for c in range(Cf): # casi sempre veri
        N = random.randint(2, 1000)
        M = random.randint(N, 1000)
        print(str(N) + ' ' + str(M) + ' ' + str(k))
        always_true(k, M, N)
        print()

    for c in range(Cs): # casi sempre veri
        N = random.randint(2, 1000)
        M = random.randint(N, 1000)
        print(str(N) + ' ' + str(M) + ' ' + str(k))
        always_true_two(k, M, N)
        print()

def second(T, Cf, Cs):
    k = 3
    out = ''

    for t in range(T):
        N = random.randint(2, 1000)
        M = random.randint(N, 1000)
        print(str(N) + ' ' + str(M) + ' ' + str(k))

        for m in range(M):
            sequence = [str(random.randint(0,N-1)) for pos in range(k)]
            print(' '.join(sequence))
        print()

    for c in range(Cf):
        N = random.randint(2, 1000)
        M = random.randint(N, 1000)
        print(str(N) + ' ' + str(M) + ' ' + str(k))
        always_true(k, M, N)
        print()

    for c in range(Cs): # casi sempre veri
        N = random.randint(2, 1000)
        M = random.randint(N, 1000)
        print(str(N) + ' ' + str(M) + ' ' + str(k))
        always_true_two(k, M, N)
        print()

def third(T, Cf, Cs):
    k = 3
    out = ''

    for t in range(T):
        N = random.randint(2, 200)
        M = random.randint(N, 10000)
        print(str(N) + ' ' + str(M) + ' ' + str(k))

        for m in range(M):
            sequence = [str(random.randint(0,N-1)) for pos in range(k)]
            print(' '.join(sequence))
        print()

    for c in range(Cf):
        N = random.randint(2, 1000)
        M = random.randint(N, 10000)
        print(str(N) + ' ' + str(M) + ' ' + str(k))
        always_true(k, M, N)
        print()

    for c in range(Cs): # casi sempre veri
        N = random.randint(2, 1000)
        M = random.randint(N, 1000)
        print(str(N) + ' ' + str(M) + ' ' + str(k))
        always_true_two(k, M, N)
        print()

def fourth(T, Cf, Cs):
    k = random.randint(2, 10)
    out = ''

    for t in range(T):
        N = random.randint(2, 100)
        M = random.randint(N, 5000)
        print(str(N) + ' ' + str(M) + ' ' + str(k))

        for m in range(M):
            sequence = [str(random.randint(0,N-1)) for pos in range(k)]
            print(' '.join(sequence))
        print()

    for c in range(Cf):
        N = random.randint(2, 1000)
        M = random.randint(N, 10000)
        print(str(N) + ' ' + str(M) + ' ' + str(k))
        always_true(k, M, N)
        print()

    for c in range(Cs): # casi sempre veri
        N = random.randint(2, 1000)
        M = random.randint(N, 1000)
        print(str(N) + ' ' + str(M) + ' ' + str(k))
        always_true_two(k, M, N)
        print()

def always_true(k, M, N):
    customRand = lambda a, b: a if a == b else random.randint(a, b)
    first_seq = ['0' for i in range(k)]
    print(' '.join(first_seq))
    n = 1
    for m in range(M-1):
        seq = []
        for i in range(k-1):
            seq.append(str(customRand(n, N-1)))
        seq.append(str(n))
        if n == N-1:
            n = N-1
        else:
            n += 1
        print(' '.join(seq))

def always_true_two(k, M, N):
    seq = ['0' for i in range(k)]
    for n in range(N):
        seq.append(str(n))
    start = 0
    while start != M:
        if start+k < len(seq):
            row = []
            for i in range(k):
                row.append(seq[start+i])
            start += 1
            print(' '.join(row))
        else:
            seq.append(seq[len(seq)-1])
            row = []
            for i in range(k):
                row.append(seq[start + i])
            start += 1
            print(' '.join(row))

print(str(100) + '\n' + '')
first(3, 11, 11)
second(3, 11, 11)
third(3, 11, 11)
fourth(3, 11, 11)
