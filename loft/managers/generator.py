#!/usr/bin/env python3

#####
# LUISS Final Contest 2023
# Task n. 4 "Breaking into LOFT"
# INPUT GENERATOR
# Francesca Romana Sanna, Leonardo Azzi
#####

import random

# Define commands to be used in the test cases:
commands = ['{_}', '{^}', '{<}', '{>}']

# Generator parameters:

easy_range = (1, 50)

medium_range = (50, 100)

hard_range = (100, 500)

commands_range = (50, 100)


# Generate easy test cases:
def easy_case():
    input_len = random.randint(easy_range[0], easy_range[1])
    input_string = ''.join(random.choices(commands + [str(i) for i in range(1, 10)], k=input_len))
    return str(input_string)

# Generate medium test cases:
def medium_case():
    input_len = random.randint(medium_range[0], medium_range[1])
    input_string = ''.join(random.choices(commands + [str(i) for i in range(1, 10)], k=input_len))
    return str(input_string)

# Generate hard test cases:
def hard_case():
    input_len = random.randint(hard_range[0], hard_range[1])
    input_string = ''.join(random.choices(commands + [str(i) for i in range(1, 10)], k=input_len))
    return str(input_string)

# Generate edge cases:

def edge_case_1():
    # Empty input string
    return "{}"

def edge_case_down():
    # 1 Command repeated multiple times
    num_commands = random.randint(commands_range[0], commands_range[1])
    command_string = commands[0]
    input_string = command_string * num_commands
    return str(input_string)

def edge_case_up():
    # 1 Command repeated multiple times
    num_commands = random.randint(commands_range[0], commands_range[1])
    command_string = commands[1]
    input_string = command_string * num_commands
    return str(input_string)

def edge_case_left():
    # 1 Command repeated multiple times
    num_commands = random.randint(commands_range[0], commands_range[1])
    command_string = commands[2]
    input_string = command_string * num_commands
    return str(input_string)

def edge_case_right():
    # 1 Command repeated multiple times
    num_commands = random.randint(commands_range[0], commands_range[1])
    command_string = commands[3]
    input_string = command_string * num_commands
    return str(input_string)

def edge_case_3():
    # Cursor moving out of bounds
    input_len = random.randint(commands_range[0], commands_range[1])
    input_string = ''.join(random.choices(commands, k=input_len))
    return str(input_string + random.choice(commands))

CASES = [easy_case]*4 + [medium_case]*6 + [hard_case]*6 + [edge_case_1]*2 + [edge_case_down] + [edge_case_up] + [edge_case_left] + [edge_case_right] + [edge_case_3]*3

print(len(CASES))

for x in CASES:
    print()
    print(str(x()))

