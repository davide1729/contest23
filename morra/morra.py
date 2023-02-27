import random

players_list = [] # list containing all the players
rounds_list = [] # list containing all the rounds
num_thrown = {} # dict containing numbers thrown by each player at each round
num_announced = {} # dict containing numbers announced by each player at each round
sum_counter = {} # dict containing the sum of all the numbers thrown per round
num_announced = {} # dict containing all the numbers announced loudly by each player

n = 3 # number of players
m = 3 # number of rounds

# creating a list with all players
for i in range(n):
    players_list.append(f"player{i}")

# creating a list with all the rounds
for round in range(m):
    rounds_list.append(f"round{round}")

# instantiating a dictionary recording all the numbers thrown by each player
for player in players_list:
    num_thrown[player] = []

# filling in the two dictionaries (namely num_thrown and sum_counter)
# num_thrown: records all the numbers thrown by each player
# sum_counter: records the sum of all the numbers thrown per round
for round in rounds_list:
    sum_round = 0
    for player in players_list:
        number_thrown = random.randint(0,10)
        sum_round += number_thrown
        num_thrown[player].append(number_thrown)
    sum_counter[round] = sum_round

# instantiating a dictionary recording all the numbers announced by each player
for player in players_list:
    num_announced[player] = []

# filling in a dictionary (namely num_announced) containing all the numbers announced by the players at each round
for round in rounds_list:
    for player in players_list:
        number_announced = random.randint(0, 10*n)
        num_announced[player].append(number_announced)


#print(players_list)
#print(rounds_list)
#print(num_thrown) 
print(sum_counter)
print(num_announced)

# creating a list containing the sum of all the numbers thrown per round. Each index corresponds to a round
sum_lst = list(sum_counter.values())
print(sum_lst)

# creating a counter for each player
player_counter = {}
for player in players_list:
    player_counter[player] = 0
print(player_counter)

'''
for player in num_announced:
    round = 0
    while round <= m:
        if num_announced[player][round] == sum_lst[round]:
            player_counter[player] += 1
    round += 1
#print(player_counter)
'''

for player in num_announced:
    for round in range(m):
        if num_announced[player][round] == sum_lst[round]:
            player_counter[player] += 1
print(player_counter)


# sorting the dictionary player counter by values in descending order
player_counter_sorted = sorted(player_counter.items(), key=lambda x:x[1], reverse=True)
player_counter_converted = dict(player_counter_sorted)
print(player_counter_converted)

# showing the final ranking
players_ranking = [] # list containing players ordered according to the score they got. The first players are those who achieved better results
winners = [] # list containing the winners

if sum(player_counter_converted.values()) != 0:
    for player in player_counter_converted:
        players_ranking.append(player)
    winners.append(players_ranking[0])
    for player in player_counter_converted:
        if player_counter_converted[player] == player_counter_converted[winners[0]] and player != winners[0]:
            winners.append(player)
        elif player_counter_converted[player] == player_counter_converted[winners[0]] and player == winners[0]:
            continue
    print(winners)
else:
    print(None)

# displaying the winners
if len(winners) != 0:
    for player in winners:
        print(player)
