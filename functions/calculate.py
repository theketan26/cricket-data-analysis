import pandas as pd
import numpy as np
from json import load


'''
find_sr(player, type)
Finds strike rate of a player in specified format

get_last_ten(player, type)
Finds record of last 10 record

performance_batsman(player, type, oppositions)
Finds performance of player in specified format against oppositions bowlers

performance_bowler(player, type, oppositions)
Finds performance of player in specified format against oppositions batsmen
'''


def find_sr(player, type):
    print('Starting to find strike-rate!')

    players = {}
    with open('../data/json/batsmen.json', 'r') as file:
        players = load(file)

    player = players[player]

    print('Analysing strike-rate ompleted without error!')
    return 'Completed without error!'


def performance_batsman(teams, player_name, match_type, oppositions):
    player_data = pd.read_json(f'../data/json/{match_type.lower()}_batsmen.json')[player_name]
    matches = np.array(player_data['matches'][::-1])

    innings = []
    last_ten_innings = []
    wickets = 0

    i = 10

    for match in matches:
        with open(f'../data/json/{match}.json') as file:
            data = load(file)

        runs, balls = 0, 0

        for inning in data['innings']:
            for over in inning['overs']:
                for delivery in over['deliveries']:
                    if delivery['batter'] == player_name:
                        if 'wickets' not in delivery.keys():
                            runs += delivery['runs']['batter']
                            balls += 1
                        else:
                            wickets += 1

        if i:
            last_ten_innings.append([runs, balls])
            i -= 1
        innings.append([runs, balls])

    avg = player_data['runs'] / wickets
    sr = player_data['runs'] / player_data['balls']

    last_ten_runs = sum(map(lambda x: x[0], last_ten_innings))
    last_ten_balls = sum(map(lambda x: x[1], last_ten_innings))
    last_ten_sr = last_ten_runs / last_ten_balls
    last_ten_avg = last_ten_runs / 10

    rates = {
        'player_name': player_name,
        'batting_experience': len(matches),
        'batting_runs': player_data['runs'],
        'batting_average': avg,
        'strikerate': sr,
        'batting_runs_last_ten': last_ten_runs,
        'batting_average_last_ten': last_ten_avg,
        'strikerate_last_ten': last_ten_sr
    }

    return rates


def performance_bowler(teams, player_name, match_type, oppositions):
    player_data = pd.read_json(f'../data/json/{match_type.lower()}_bowler.json')[player_name]
    matches = np.array(player_data['matches'][::-1])

    innings = []
    last_ten_innings = []
    total_wicket = 0

    i = 10

    for match in matches:
        with open(f'../data/json/{match}.json') as file:
            data = load(file)

        runs, wicket = 0, 0

        for inning in data['innings']:
            for over in inning['overs']:
                for delivery in over['deliveries']:
                    if delivery['bowler'] == player_name:
                        if 'wickets' not in delivery.keys():
                            runs += delivery['runs']['batter']
                        else:
                            wicket += 1
                            total_wicket += 1

        if i:
            last_ten_innings.append([runs, wicket])
            i -= 1
        innings.append([runs, wicket])

    avg = sum(map(lambda x: x[0], innings)) / len(matches)
    avg_last_ten = sum(map(lambda x: x[0], last_ten_innings)) / 10
    wickets_avg = sum(map(lambda x: x[1], innings)) / len(matches)
    wickets_avg_last_ten = sum(map(lambda x: x[1], last_ten_innings)) / 10

    if avg_last_ten < 20:
        temp = 1
    elif (1 - (avg_last_ten / 40)) < 0:
        temp = 0
    else:
        temp = 1 - (avg_last_ten / 40)

    rates = {
        'player_name': player_name,
        'bowling_experience': len(matches),
        'bowling_average': avg,
        'wicket': total_wicket,
        'wicket_average': wickets_avg,
        'bowling_average_last_ten': temp,
        'wicket_last_ten': wickets_avg_last_ten,
    }

    return rates


def performance(teams, players, type, opposition):
    performance_batter = []
    performance_bowler_ = []
    performance_allrounder = []

    for player in players['batsman']:
        performance_batter.append(performance_batsman(teams, player, type, opposition))
    for player in players['bowler']:
        performance_bowler_.append(performance_bowler(teams, player, type, opposition))
    for player in players['allrounder']:
        temp = performance_batsman(teams, player, type, opposition)
        temp.update(performance_bowler(teams, player, type, opposition))
        performance_allrounder.append(temp)

    players_rating = {
        'batsman': {},
        'bowler': {},
        'allrounder': {}
    }

    max_states = {}
    for key in list(performance_batter[0].keys())[1:]:
        temp = 0
        for player in performance_batter:
            if player[key] > temp:
                temp = player[key]
        max_states[key] = temp if temp != 0 else .00001

    for player in performance_batter:
        rating = (player['batting_runs'] / max_states['batting_runs']) / 20
        rating += (player['batting_average'] / max_states['batting_average']) / 15
        rating += (player['strikerate'] / max_states['strikerate']) / 15
        rating += (player['batting_runs_last_ten'] / max_states['batting_runs_last_ten']) / 20
        rating += (player['batting_average_last_ten'] / max_states['batting_average_last_ten']) / 15
        rating += (player['strikerate_last_ten'] / max_states['strikerate_last_ten']) / 15
        players_rating['batsman'][player['player_name']] = rating

    max_states = {}
    for key in list(performance_bowler_[0].keys())[1:]:
        temp = 0
        for player in performance_bowler_:
            if player[key] > temp:
                temp = player[key]
        max_states[key] = temp if temp != 0 else .00001

    for player in performance_bowler_:
        rating = (player['bowling_average_last_ten'] / max_states['bowling_average_last_ten']) / 30
        rating += (player['wicket_last_ten'] / max_states['wicket_last_ten']) / 30
        rating += (player['bowling_average'] / max_states['bowling_average']) / 20
        rating += (player['wicket'] / max_states['wicket']) / 20
        players_rating['bowler'][player['player_name']] = rating

    max_states = {}
    for key in list(performance_allrounder[0].keys())[1:]:
        temp = 0
        for player in performance_allrounder:
            if player[key] > temp:
                temp = player[key]
        max_states[key] = temp if temp != 0 else .00001

    for player in performance_allrounder:
        rating = (player['batting_runs'] / max_states['batting_runs']) / 10
        rating += (player['batting_average'] / max_states['batting_average']) / 7.5
        rating += (player['strikerate'] / max_states['strikerate']) / 7.5
        rating += (player['batting_runs_last_ten'] / max_states['batting_runs_last_ten']) / 10
        rating += (player['batting_average_last_ten'] / max_states['batting_average_last_ten']) / 7.5
        rating += (player['strikerate_last_ten'] / max_states['strikerate_last_ten']) / 7.5
        rating += (player['bowling_average_last_ten'] / max_states['bowling_average_last_ten']) / 15
        rating += (player['wicket_last_ten'] / max_states['wicket_last_ten']) / 15
        rating += (player['bowling_average'] / max_states['bowling_average']) / 10
        rating += (player['wicket'] / max_states['wicket']) / 10
        players_rating['allrounder'][player['player_name']] = rating

    return players_rating