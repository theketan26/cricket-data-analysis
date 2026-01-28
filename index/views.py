from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
import json


from .form import StateForm, TeamForm, OneBatsmanForm, OneBowlerForm, OneAllrounderForm, TwoBatsmanForm, TwoBowlerForm, TwoAllrounderForm


def home(request):
    return render(request, "index.html")


def stats(request):
    form = StateForm()

    url = "http://localhost:8000/data/getTeams/"
    payload = json.dumps({
        "type": "odi"
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    teams = json.loads(response.text)['teams']

    if len(teams) == 0:
        return render(request, 'error.html', {})

    url = "http://localhost:8000/data/getPlayers/"
    payload = json.dumps({
        "team": "All",
        "type": "ODI"
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    data = json.loads(response.text)
    players = data['batsman'] + data['bowler']
    roles = ['batting', 'bowling', 'allrounder']

    player_choices = [(p, p) for p in players]
    role_choices = [(r, r) for r in roles]

    form = StateForm(player_choices=player_choices, role_choices=role_choices)

    context = {
        'types': ['ODI', 'T20', 'Test'],
        'teams': teams,
        'players': players,
        'roles': ['Batting', 'Bowling', 'Allrounder'],
        'form': form
    }

    return render(request, "states.html", context)


def state_result(request):
    try:
        # Fetch players and roles for form choices
        url = "http://localhost:8000/data/getPlayers/"
        payload = json.dumps({
            "team": "All",
            "type": "ODI"
        })
        headers = {
          'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        data = json.loads(response.text)
        players = data['batsman'] + data['bowler']
        roles = ['batting', 'bowling', 'allrounder']

        player_choices = [(p, p) for p in players]
        role_choices = [(r, r) for r in roles]

        form = StateForm(request.POST, player_choices=player_choices, role_choices=role_choices)

        if form.is_valid():
            player = form.cleaned_data['player']
            role = form.cleaned_data['role']

            url = 'http://localhost:8000/data/getPlayerState/'
            playload = json.dumps({
                "type": 'ODI',
                "team": [],
                "player": player,
                "role": role
            })
            header = {
                'Content-Type': 'application/json'
            }
            response = requests.request('POST', url, headers=header, data=playload)
            response = json.loads(response.text)

        return render(request, 'state_result.html', response)
    except:
        return render(request, 'error.html', {})


def predict_pre(request):
    try:
        url = "http://localhost:8000/data/getTeams/"
        payload = json.dumps({
            "type": "ODI"
        })
        headers = {
          'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        teams = (json.loads(response.text))['teams']

        context = {
            'teams': teams,
            'form': TeamForm,
            'types': ['ODI', 'T20', 'Test'],
        }
        return render(request, 'predict_pre.html', context)
    except:
        return render(request, 'error.html', {})


def predict(request):
    try:
        data = TeamForm(request.POST)
        if data.is_valid():
            url = "http://localhost:8000/data/getPlayers/"
            payload = json.dumps({
                "team": data.cleaned_data['one'],
                "type": data.cleaned_data['type']
            })
            headers = {
              'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            one = json.loads(response.text)
            team_one = one['batsman'] + one['bowler']

            url = "http://localhost:8000/data/getPlayers/"
            payload = json.dumps({
                "team": data.cleaned_data['two'],
                "type": data.cleaned_data['type']
            })
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            two = json.loads(response.text)
            team_two = two['batsman'] + two['bowler']

        teams = [team_one, team_two]
        context = {
            'team_one': team_one,
            'team_two': team_two,
            'one': data.cleaned_data['one'],
            'two': data.cleaned_data['two'],
            'one_batsman_form': OneBatsmanForm(),
            'one_bowler_form': OneBowlerForm(),
            'one_allrounder_form': OneAllrounderForm(),
            'two_batsman_form': TwoBatsmanForm(),
            'two_bowler_form': TwoBowlerForm(),
            'two_allrounder_form': TwoAllrounderForm(),
        }
        return render(request, 'predict.html', context)
    except:
        return render(request, 'error.html', {})


def predict_result(request):
    try:
        if request.method == 'POST':
            forms = {
                'team_one_batsman': OneBatsmanForm(request.POST),
                'team_one_bowler': OneBowlerForm(request.POST),
                'team_one_allrounder': OneAllrounderForm(request.POST),
                'team_two_batsman': TwoBatsmanForm(request.POST),
                'team_two_bowler': TwoBowlerForm(request.POST),
                'team_two_allrounder': TwoAllrounderForm(request.POST),
            }

            data = {}
            for key in forms.keys():
                if forms[key].is_valid():
                    lst = forms[key].cleaned_data
                    data[key] = list(filter(lambda x: x != '', map(lambda x: lst[x], lst.keys())))

            players = {}
            for key in list(data.keys())[:3]:
                role = (key.split('_'))[-1]
                players[role] = data[key]
            url = 'http://localhost:8000/data/analyse/'
            playload = json.dumps({
                'teams': [],
                'players': players,
                'type': 'ODI',
                'opposition': []
            })
            header = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=header, data=playload)
            team_one_players = json.loads(response.text)

            for key in list(data.keys())[3:]:
                role = (key.split('_'))[-1]
                players[role] = data[key]
            url = 'http://localhost:8000/data/analyse/'
            playload = json.dumps({
                'teams': [],
                'players': players,
                'type': 'ODI',
                'opposition': []
            })
            header = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=header, data=playload)
            team_two_players = json.loads(response.text)

            team_one_players['batsman'].update(team_two_players['batsman'])
            team_one_players['bowler'].update(team_two_players['bowler'])
            team_one_players['allrounder'].update(team_two_players['allrounder'])

            players = {
                'batsman': enumerate(sorted(team_one_players['batsman'].items(), key=lambda x: x[1])[::-1]),
                'bowler': enumerate(sorted(team_one_players['bowler'].items(), key=lambda x: x[1])[::-1]),
                'allrounder': enumerate(sorted(team_one_players['allrounder'].items(), key=lambda x: x[1])[::-1])
            }

        return render(request, 'predict_result.html', players)
    except:
        return render(request, 'error.html', {})
