#!/usr/bin/env python3

#
# Generator Final Contest LUISS ... 2023
# Task n. x "Nome completo task"
# autori
#

# import librerie necessarie

T = float(input()) # 25
assert T == int(T)
T = int(T)
assert 0 <= T <= 25
for t in range(T):
    assert input() == "" # spazio vuoto
    # controlla tutti gli altri