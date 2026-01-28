from json import load


from .calculate import performance_batsman, performance_bowler


def teams(type):
    with open(f'data/json/players.json', 'r') as file:
        teams = load(file)

    return list(teams.keys())


def players(team, type):
    with open(f'data/json/players.json', 'r') as file:
        if team != 'All':
            players = list(load(file)[team])
        else:
            players = []
            data = load(file)
            for team in data.keys():
                players += data[team]

    with open(f'data/json/{type.lower()}_batsmen.json', 'r') as file:
        batsman = filter(lambda x: True if x in players else False, list(load(file).keys()))
    with open(f'data/json/{type.lower()}_bowler.json', 'r') as file:
        bowler = filter(lambda x: True if x in players else False, list(load(file).keys()))

    response = {
        'batsman': list(batsman),
        'bowler': list(bowler)
    }

    return response


def player_state(type, team, player, role):
    role = role.lower()
    if role == 'batting':
        print(team, player, type)
        response = performance_batsman([team, ''], player, type, [])
        response['role'] = 'batsman'
    elif role == 'bowling':
        response = performance_bowler(['', team], player, type, [])
        response['role'] = 'bowler'
    elif role == 'allrounder':
        response = performance_batsman([team, ''], player, type, [])
        r_two = performance_bowler(['', team], player, type, [])
        response.update(r_two)
        response['role'] = 'allrounder'

    return response



