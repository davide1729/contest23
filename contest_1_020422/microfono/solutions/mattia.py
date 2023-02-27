#!/usr/bin/env python3

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0] * p2[1] - p2[0] * p1[1])
    return A, B, -C


def intersection(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x, y
    else:
        return False


N = int(input())
for case in range(N):
    input()
    nmuri = int(input())
    micstring = input()
    miclist = [int(x) for x in micstring.strip().split(" ")]
    mic1 = (miclist[0], miclist[1])
    mic2 = (miclist[2], miclist[3])
    vert = False
    interlist = []
    mind = 0
    micline = line(mic1, mic2)
    for nmuro in range(nmuri):
        murostring = input()
        murolist = [int(x) for x in murostring.strip().split(" ")]
        pmuro1 = (murolist[0], murolist[1])
        pmuro2 = (murolist[2], murolist[3])
        highx = max(pmuro1[0], pmuro2[0])
        lowx = min(pmuro1[0], pmuro2[0])
        highy = max(pmuro1[1], pmuro2[1])
        lowy = min(pmuro1[1], pmuro2[1])
        muroline = line(pmuro1, pmuro2)
        inter = intersection(micline, muroline)
        if inter:
            xint = inter[0]
            yint = inter[1]
            if (lowx <= xint <= highx) and (lowy <= yint <= highy):
                if mic2[0] > mic1[0] and xint > mic1[0]:
                    interlist.append(inter)
                elif mic2[0] < mic1[0] and xint < mic1[0]:
                    interlist.append(inter)
                elif mic2[0] == mic1[0]:
                    vert = True
                    if mic1[1] < mic2[1] and yint > mic1[1]:
                        interlist.append(inter)
                    elif mic1[1] > mic2[1] and yint < mic1[1]:
                        interlist.append(inter)
    if interlist:
        if vert:
            best = interlist[0]
            mind = abs(best[1] - mic1[1])
            for el in interlist:
                if abs(el[1] - mic1[1]) < mind:
                    mind = abs(el[1] - mic1[1])
                    best = el
        else:
            best = interlist[0]
            mind = abs(best[0] - mic1[0])
            for el in interlist:
                if abs(el[0] - mic1[0]) < mind:
                    mind = abs(el[0] - mic1[0])
                    best = el
        sqdist = (best[0] - mic1[0]) ** 2 + (best[1] - mic1[1]) ** 2
        print(f"Case #{case + 1}: {int(sqdist)}")
    else:
        print(f"Case #{case + 1}: LOFT")

