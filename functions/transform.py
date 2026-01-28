from ..models import Matches
from json import load, dump


'''
transformpLayers()
This function extract useful information from records of matches and
store in batsmen.json and bowler.json files

transformformatplayers()
This function extract data of players of only specified formate 
matches

'''


def  transformplayers():
    matches = Matches.objects.all()

    size, n = len(matches), 1

    batter_players = {}
    bowling_players = {}

    print('Starting transformation of player data!')

    for match in matches:
        print(n, '/', size, end='    ')
        n += 1
        id = match.match_id
        print(f'Running for match id {id}')

        file = open(f'data/json/{id}.json')
        dic = load(file)
        info = dic['info']

        type = info['match_type']
        teams = info['teams']
        winner = info['outcome'][list(info['outcome'].keys())[0]]
        venue = info['venue']

        team_meta = {
            'type': type,
            'teams': teams,
            'winner': winner,
            'venue': venue
        }

        innings = dic['innings']

        for inning in innings:
            team = inning['team']

            for over in inning['overs']:
                for delivery in over['deliveries']:
                    batter = delivery['batter']
                    bowler = delivery['bowler']
                    runs = 0
                    wicket = False
                    four = False
                    six = False

                    if 'wickets' in delivery.keys():
                        wicket = True
                        runs = delivery['runs']['total']
                    else:
                        runs = delivery['runs']['batter']
                        if runs == 4:
                            four = True
                        elif runs == 6:
                            six = True

                    if wicket:
                        if bowler in bowling_players.keys():
                            bowling_players[bowler]['balls'] += 1
                            bowling_players[bowler]['wickets'] += 1
                            bowling_players[bowler]['runs_given'] += runs
                            if id not in bowling_players[bowler]['matches']:
                                bowling_players[bowler]['matches'].append(id)
                            if batter in bowling_players[bowler].keys():
                                bowling_players[bowler][batter] += 1
                            else:
                                bowling_players[bowler][batter] = 1

                        else:
                            bowling_players[bowler] = {
                                'balls': 1,
                                'wickets': 1,
                                'runs_given': runs,
                                'matches': [id]
                            }
                            if batter in bowling_players[bowler].keys():
                                bowling_players[bowler][batter] += 1
                            else:
                                bowling_players[bowler][batter] = 1


                    else:
                        if batter not in batter_players.keys():
                            batter_players[batter] = {
                                'runs': runs,
                                'balls': 1,
                                'four': 1 if four else 0,
                                'six': 1 if six else 0,
                                'matches': [id]
                            }
                            if bowler in batter_players[batter].keys():
                                batter_players[batter][bowler] += runs
                            else:
                                batter_players[batter][bowler] = runs

                        else:
                            batter_players[batter]['runs'] += runs
                            batter_players[batter]['balls'] += 1
                            batter_players[batter]['four'] += 1 if four else 0
                            batter_players[batter]['six'] += 1 if six else 0
                            if id not in batter_players[batter]['matches']:
                                batter_players[batter]['matches'].append(id)
                            if bowler in batter_players[batter].keys():
                                batter_players[batter][bowler] += runs
                            else:
                                batter_players[batter][bowler] = runs

                        if bowler in bowling_players.keys():
                            bowling_players[bowler]['balls'] += 1
                            bowling_players[bowler]['runs_given'] += runs
                            if id not in bowling_players[bowler]['matches']:
                                bowling_players[bowler]['matches'].append(id)
                        else:
                            bowling_players[bowler] = {
                                'balls': 1,
                                'wickets': 0,
                                'runs_given': runs,
                                'matches': [id]
                            }

    with open('data/json/batsmen.json', 'w') as file:
        dump(batter_players ,file)
    with open('data/json/bowlers.json', 'w') as file:
        dump(bowling_players, file)

    print('Completed without error!')
    return 'Completed'


def transformformatplayers(format):
    print(f'Starting transforming {format} data!')

    matches = Matches.objects.filter(type=format)

    size, n = len(matches), 1

    batter_players = {}
    bowling_players = {}

    for match in matches:
        print(n, '/', size, end='    ')
        n += 1
        id = match.match_id
        print(f'Running for match id {id}')

        file = open(f'data/json/{id}.json')
        dic = load(file)
        info = dic['info']

        type = info['match_type']
        teams = info['teams']
        winner = info['outcome'][list(info['outcome'].keys())[0]]
        venue = info['venue']

        team_meta = {
            'type': type,
            'teams': teams,
            'winner': winner,
            'venue': venue
        }

        innings = dic['innings']

        for inning in innings:
            team = inning['team']

            for over in inning['overs']:
                for delivery in over['deliveries']:
                    batter = delivery['batter']
                    bowler = delivery['bowler']
                    runs = 0
                    wicket = False
                    four = False
                    six = False

                    if 'wickets' in delivery.keys():
                        wicket = True
                        runs = delivery['runs']['total']
                    else:
                        runs = delivery['runs']['batter']
                        if runs == 4:
                            four = True
                        elif runs == 6:
                            six = True

                    if wicket:
                        if bowler in bowling_players.keys():
                            bowling_players[bowler]['balls'] += 1
                            bowling_players[bowler]['wickets'] += 1
                            bowling_players[bowler]['runs_given'] += runs
                            if id not in bowling_players[bowler]['matches']:
                                bowling_players[bowler]['matches'].append(id)
                            if batter in bowling_players[bowler].keys():
                                bowling_players[bowler][batter] += 1
                            else:
                                bowling_players[bowler][batter] = 1

                        else:
                            bowling_players[bowler] = {
                                'balls': 1,
                                'wickets': 1,
                                'runs_given': runs,
                                'matches': [id]
                            }
                            if batter in bowling_players[bowler].keys():
                                bowling_players[bowler][batter] += 1
                            else:
                                bowling_players[bowler][batter] = 1


                    else:
                        if batter not in batter_players.keys():
                            batter_players[batter] = {
                                'runs': runs,
                                'balls': 1,
                                'four': 1 if four else 0,
                                'six': 1 if six else 0,
                                'matches': [id]
                            }
                            if bowler in batter_players[batter].keys():
                                batter_players[batter][bowler] += runs
                            else:
                                batter_players[batter][bowler] = runs

                        else:
                            batter_players[batter]['runs'] += runs
                            batter_players[batter]['balls'] += 1
                            batter_players[batter]['four'] += 1 if four else 0
                            batter_players[batter]['six'] += 1 if six else 0
                            if id not in batter_players[batter]['matches']:
                                batter_players[batter]['matches'].append(id)
                            if bowler in batter_players[batter].keys():
                                batter_players[batter][bowler] += runs
                            else:
                                batter_players[batter][bowler] = runs

                        if bowler in bowling_players.keys():
                            bowling_players[bowler]['balls'] += 1
                            bowling_players[bowler]['runs_given'] += runs
                            if id not in bowling_players[bowler]['matches']:
                                bowling_players[bowler]['matches'].append(id)
                        else:
                            bowling_players[bowler] = {
                                'balls': 1,
                                'wickets': 0,
                                'runs_given': runs,
                                'matches': [id]
                            }

    with open(f'data/json/{format.lower()}_batsmen.json', 'w') as file:
        dump(batter_players ,file)
    with open(f'data/json/{format.lower()}_bowler.json', 'w') as file:
        dump(bowling_players, file)

    print('Completed without error!')


def extract_teams():
    matches = Matches.objects.all()

    size, n = len(matches), 1

    players = {}

    print('Starting extracting teams!')

    for match in matches:
        print(n, '/', size, end='    ')
        n += 1
        id = match.match_id
        print(f'Running for match id {id}')

        file = open(f'data/json/{id}.json')
        dic = load(file)
        info = dic['info']['players']
        teams = list(info.keys())

        if teams[0] not in players:
            players[teams[0]] = []
        if teams[1] not in players:
            players[teams[1]] = []

        for player in info[teams[0]]:
            if player not in players[teams[0]]:
                players[teams[0]].append(player)
        for player in info[teams[1]]:
            if player not in players[teams[1]]:
                players[teams[1]].append(player)

    with open(f'data/json/players.json', 'w') as file:
        dump(players, file)

    return players

