#!/usr/bin/env python3
# Generator Task 3: Calendario accademico
# Lorenzo Organtini | Mattia Cervellini

import random

def simple():
    n = random.randint(10, 100)
    k = 1

    students = [random.randint(0, 100) for i in range(n)]
    return n, k, students

def medium():
    n = random.randint(10, 1000)
    k = 2

    students = [random.randint(0, 1000) for i in range(n)]
    return n, k, students

def complicated():
    n = random.randint(10, 1000)
    k = random.randint(1, int(n/2)-1)

    students = [random.randint(0, 10000) for i in range(n)]
    return n, k, students

def every_increase():
    n = random.randint(10, 1000)
    k = int(n/2+1)

    students = [random.randint(0, 10000) for i in range(n)]
    return n, k, students

def rompi_quadratiche():
    n = random.randint(900, 1100)
    k = random.randint(3, int(n/2)-1)

    students = [random.randint(0, 100000) for i in range(n)]
    return n, k, students

def edge_case_increasing():
    n = random.randint(10, 10**6)
    k = int(n/2+1)

    students = []
    start = random.randint(0, 10)
    for i in range(n):
        students.append(start)
        start += random.randint(1, 5)
    return n, k, students

def edge_case_decreasing(): 
    n = random.randint(10, 10**7)
    k = int(n/2+1)

    students = []
    start = random.randint(70000, 10**7)
    for i in range(n):
        if start == 0:
            students.append(start)
        else:
            students.append(start)
            candidate = start - random.randint(1, 5)
            if candidate < 0:
                start = 0
            else:
                start = candidate
    return n, k, students

def inputfile():
    inp = '25' + '\n' + '' + '\n'
    counter_i = random.randint(0, 13) # to randomly assign the edge cases
    counter_d = random.randint(0, 13)
    while (counter_d==counter_i):
        counter_d = random.randint(0, 13)
    step = 0

    n_i, k_i, students = edge_case_increasing() # pre-generating edge cases
    increasing_str = [str(x) for x in students]

    n_d, k_d, students = edge_case_decreasing()
    decreasing_str = [str(x) for x in students]

    # simple case: 4 points
    for i in range(4):
        n, k, students = simple()
        students_str = [str(x) for x in students]
        inp += str(n) + ' ' + str(k) + '\n'
        inp += ' '.join(students_str) + '\n' + '' + '\n'

    # k = 2 case: 6 points
    for i in range(6):
        n, k, students = medium()
        students_str = [str(x) for x in students]
        inp += str(n) + ' ' + str(k) + '\n'
        inp += ' '.join(students_str) + '\n' + '' + '\n'

    # complicated: 10 points
    for i in range(5):
        n, k, students = complicated()
        students_str = [str(x) for x in students]
        inp += str(n) + ' ' + str(k) + '\n'
        inp += ' '.join(students_str) + '\n' + '' + '\n'

        if counter_i == step:
            inp += str(n_i) + ' ' + str(k_i) + '\n'
            inp += ' '.join(increasing_str) + '\n' + '' + '\n'
        elif counter_d == step:
            inp += str(n_d) + ' ' + str(k_d) + '\n'
            inp += ' '.join(decreasing_str) + '\n' + '' + '\n'
        step += 1

    for i in range(5):
        n, k, students = rompi_quadratiche()
        students_str = [str(x) for x in students]
        inp += str(n) + ' ' + str(k) + '\n'
        inp += ' '.join(students_str) + '\n' + '' + '\n'

        if counter_i == step:
            inp += str(n_i) + ' ' + str(k_i) + '\n'
            inp += ' '.join(increasing_str) + '\n' + '' + '\n'
        elif counter_d == step:
            inp += str(n_d) + ' ' + str(k_d) + '\n'
            inp += ' '.join(decreasing_str) + '\n' + '' + '\n'
        step += 1

    # simple that looks complicated: 5 points
    for i in range(3):
        n, k, students = every_increase()
        students_str = [str(x) for x in students]
        inp += str(n) + ' ' + str(k) + '\n'
        inp += ' '.join(students_str) + '\n' + '' + '\n'

        if counter_i == step:
            inp += str(n_i) + ' ' + str(k_i) + '\n'
            inp += ' '.join(increasing_str) + '\n' + '' + '\n'
        elif counter_d == step:
            inp += str(n_d) + ' ' + str(k_d) + '\n'
            inp += ' '.join(decreasing_str) + '\n' + '' + '\n'
        step += 1

    if counter_i == step:
        inp += str(n_i) + ' ' + str(k_i) + '\n'
        inp += ' '.join(increasing_str) + '\n' + '' + '\n'
    elif counter_d == step:
        inp += str(n_d) + ' ' + str(k_d) + '\n'
        inp += ' '.join(decreasing_str) + '\n' + '' + '\n'

    return inp


input_str = inputfile()
print(input_str)