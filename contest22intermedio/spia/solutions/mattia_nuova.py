#!/usr/bin/env python3

def hack(drone, dronivivi):
    index = drone[1]
    if drone not in dronivivi:
        return 0
    if (n-1)/2 <= index <= n-1:
        dronivivi.remove(drone)
        return 2
    dronivivi.remove(drone)
    return 2+hack((inlist[index*2+1], index*2+1), dronivivi)+hack((inlist[index*2+2], index*2+2), dronivivi)

ncasi = int(input())
for caso in range(ncasi):
    input()
    sol = f"Case #{caso+1}: "
    nscasi= int(input())
    for scaso in range(nscasi):
        row = input()
        inlist = [int(x) for x in row.strip().split()]
        n = inlist[0]
        inlist = inlist[1:]
        dronivivi = []
        chrono = 0
        fail = False
        for k, val in enumerate(inlist):
            dronivivi.append((val, k))
        dronivivi.sort(key=lambda i:i[0])
        while len(dronivivi) > 0:
            primodrone = dronivivi[0]
            timeneeded = hack(primodrone, dronivivi)
            chrono += timeneeded
            if chrono > primodrone[0]:
                fail = True
                break
        if fail:
            sol += "Luiss_LOFT "
        else:
            sol += "Droni_disattivati "
    sol = sol[:-1]
    print(sol)

