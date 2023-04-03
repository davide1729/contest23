#!/usr/bin/env python3

# Generator Task 2: Droni spia
# Lorenzo Organtini

import random

tests = 4
T = 25

print(T*tests)

for test in range(tests): # definisce grupoo di casi di test
    out = ''

    for t in range(T): # per ogni caso di test
        C = 5 # genera i sottocasi di test
        out += '\n' + str(C) + '\n'

        for c in range(C): # per ogni sottocaso di test
            if test == 0:  # genera N
                i = random.randint(1, 3)
            elif test == 1 or test == 2:
                i = random.randint(1,12)
            else:
                i = random.randint(1, 16)
            N = 2**i-1
            
            if test == 0: # genera tempi dei droni nel primo caso
                tempi = [random.randint(1, 30) for n in range(N)] # circa 2 volte il 14
            elif test == 2 or test == 3: # genera tempi dei droni se fuori dal secondo caso
                tempi = [random.randint(1, 100000) for n in range(N)]
            else:
                tempi = [random.randint(1, 100000)] # genera l'ultimo drone
                if i > 2:
                    index = 0
                    flag = True
                    while flag:
                        new_f = random.randint(1, tempi[index]) # genera droni 1 e 2 nell'albero
                        new_s = random.randint(1, tempi[index])
                        tempi.append(new_f) # appende alla lista
                        tempi.append(new_s)

                        index += 1 # va al ramo 1
                        if len(tempi) == N:
                            flag = False

                    tempi.reverse() # la vogliamo con l'ultimo alla fine
                    
                elif i == 2:
                    tempi = [random.randint(1, 100000) for volte in range(3)]
                    tempi.sort()

            tempi_str = [str(x) for x in tempi]
            out += str(N) + ' ' + ' '.join(tempi_str) + '\n'
    print(out, end="")
            
