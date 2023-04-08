import random

def generate_test_cases(num_cases, min_len, max_len):
    test_cases = []
    commands = ['{_}', '{^}', '{<}', '{>}']
    
    for _ in range(num_cases):
        input_len = random.randint(min_len, max_len)
        input_string = ""
        
        for _ in range(input_len):
            if random.random() < 0.5:   # Adjust the probability of digits
                                        #vs. commands (0.5 should mean 50% chance of a digit)
                input_string += str(random.randint(1, 9))
            else:
                input_string += random.choice(commands)
        
        test_cases.append(input_string)
    
    return test_cases

num_cases = 5
min_len = 10
max_len = 30

test_cases = generate_test_cases(num_cases, min_len, max_len)
test_dict = {}
for i, test_case in enumerate(test_cases):
    test_dict[f"Test Case {i}"] = test_case
    print(f"Test case {i + 1}: {test_case}")

print(test_dict)
