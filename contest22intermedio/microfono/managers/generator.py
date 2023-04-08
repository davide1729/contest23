#!/usr/bin/env python3
# Generator Task 3: Microfoni
# Lorenzo Organtini

import random

def first(T):
    out = ''
    for test in range(T):
        N = 25
        out += str(N) + '\n'

        # coordinate microfono
        x = random.randint(-100, 100)
        y = 0
        a = random.randint(-100, 100)
        b = 0
        out += str(x) + ' ' + str(y) + ' ' + str(a) + ' ' + str(b) + '\n'

        for n in range(N):
            # coordinate pannelli
            r = random.randint(-100, 100)
            s = random.randint(-100, 100)
            pa = (r, s)
            t = random.randint(-100, 100)
            u = random.randint(-100, 100)
            pb = (t, u)
            while pa == pb: # no casi limite dove il pannello è un punto
                t = random.randint(-100, 100)
                u = random.randint(-100, 100)
                pb = (t, u)

            out += str(r) + ' ' + str(s) + ' ' + str(t) + ' ' + str(u) + '\n'

        if test == T-1:
            out += ''
        else:
            out += '' + '\n'

    print(out)

def second(T): # y di mic e y di punto uguali
    out = ''
    for test in range(T):
        N = 100
        out += str(N) + '\n'

        # coordinate microfono
        x = random.randint(-1000, 1000)
        y = random.randint(-1000, 1000)
        a = random.randint(-1000, 1000)
        while a == x:
            a = random.randint(-1000, 1000)
        out += str(x) + ' ' + str(y) + ' ' + str(a) + ' ' + str(y) + '\n'

        for n in range(N):
            # coordinate pannelli
            r = random.randint(-800, 800)
            s = r + random.randint(-800, 800)
            altezza = random.randint(-200, 200)
            t = s + altezza
            u = r + altezza
            out += str(r) + ' ' + str(s) + ' ' + str(t) + ' ' + str(u) + '\n'

        if test == T-1:
            out += ''
        else:
            out += '' + '\n'

    print(out)

def third(T):
    out = ''
    for test in range(T):
        N = 25000
        out += str(N) + '\n'

        # coordinate microfono
        x = random.randint(-100000, 100000)
        y = random.randint(-100000, 100000)
        px = (x, y)
        a = random.randint(-100000, 100000)
        b = random.randint(-100000, 100000)
        py = (a, b)
        while px == py:
            a = random.randint(-100000, 100000)
            b = random.randint(-100000, 100000)
            py = (a, b)
        out += str(x) + ' ' + str(y) + ' ' + str(a) + ' ' + str(b) + '\n'

        for n in range(N):
            # coordinate pannelli
            r = random.randint(-100000, 100000)
            s = random.randint(-100000, 100000)
            pa = (r, s)
            t = random.randint(-100000, 100000)
            u = random.randint(-100000, 100000)
            pb = (t, u)
            while pa == pb: # no casi limite dove il pannello è un punto
                t = random.randint(-100000, 100000)
                u = random.randint(-100000, 100000)
                pb = (t, u)

            out += str(r) + ' ' + str(s) + ' ' + str(t) + ' ' + str(u) + '\n'

        if test == T-1:
            out += ''
        else:
            out += '' + '\n'

    print(out)

def fourth(T):
    out = ''
    for test in range(T):
        N = 50000
        out += str(N) + '\n'

        # coordinate microfono
        x = random.randint(-1000000, 1000000)
        y = random.randint(-1000000, 1000000)
        a = random.randint(-1000000, 1000000)
        b = random.randint(-1000000, 1000000)
        out += str(x) + ' ' + str(y) + ' ' + str(a) + ' ' + str(b) + '\n'

        for n in range(N):
            # coordinate pannelli
            r = random.randint(-1000000, 1000000)
            s = random.randint(-1000000, 1000000)
            pa = (r, s)
            pb = (r, s)
            while pa == pb: # no casi limite dove il pannello è un punto
                t = random.randint(-1000000, 1000000)
                u = random.randint(-1000000, 1000000)
                pb = (t, u)

            out += str(r) + ' ' + str(s) + ' ' + str(t) + ' ' + str(u) + '\n'

        if test == T-1:
            out += ''
        else:
            out += '' + '\n'

    print(out)

def sempre_falso(T): # retta verticale mic e pannelli su y
    out = ''
    for test in range(T):
        N = 5
        out += str(N) + '\n'

        # coordinate microfono
        x = random.randint(-10, 10)
        while x == 0:
            x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        aggiungi = random.randint(-10, 10)
        while aggiungi == 0:
            aggiungi = random.randint(-10, 10)
        b = y + aggiungi
        out += str(x) + ' ' + str(y) + ' ' + str(x) + ' ' + str(b) + '\n'

        for n in range(N):
            # coordinate pannelli
            r = 0
            s = random.randint(-5, 5)
            add = random.randint(-5, 5)
            while add == 0:
                add = random.randint(-10, 10)
            u = s + add

            out += str(r) + ' ' + str(s) + ' ' + str(r) + ' ' + str(u) + '\n'

        if test == T-1:
            out += ''
        else:
            out += '' + '\n'

    print(out)

print(str(25) + '\n' + '')
first(5)
second(5)
third(5)
fourth(5)
sempre_falso(5)
