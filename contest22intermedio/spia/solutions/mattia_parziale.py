#!/usr/bin/env python3

chrono = 0
def hack(index):
    global chrono, hacked, timers, ndroni
    child1 = True
    child2 = True
    if index*2+2 < ndroni-1:
        next1 = index*2+1
        next2 = index*2+2
        if hacked[next1] == 0:
            child1 = hack(next1)
        if hacked[next2] == 0:
            child2 = hack(next2)
    chrono += 2
    if chrono <= timers[index] and (child1 and child2):
        hacked[index] = 1
        timers[index] = 100001
        return True
    else:
        return False

if True:
    Ncasi = int(input())
    for case in range(Ncasi):
        input()
        sol = f"case #{case + 1}: "
        if case < 51:
            nsottocasi = int(input())
            for sottoc in range(nsottocasi):
                chrono = 0
                dronisting = input()
                inputlist = [int(x) for x in dronisting.strip().split(" ")]
                ndroni = inputlist[0]
                hacked = [0 for x in range(ndroni)]
                ones = [1 for x in range(ndroni)]
                timers = inputlist[1:]
                fail = False
                while hacked != ones:
                    for c in range(len(timers)):
                        if timers[c] == min(timers) and hacked[c] == 0:
                            if not hack(c):
                                fail = True
                                break
                    if fail:
                        break
                if fail:
                    sol += "Luiss_LOFT "
                else:
                    sol += "Droni_disattivati "
            sol = sol[:-1]
        else:
            sol += "-1"
        print(sol)



