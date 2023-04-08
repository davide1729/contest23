#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. x "Nome Task"
# INPUT VALIDATOR
# Autori
#####

# import librerie necessarie

T = float(input()) # 25
assert T == int(T)
T = int(T)
assert 0 <= T <= 25
for t in range(T):
    assert input() == "" # spazio vuoto
    # controlla tutti gli altri input generati