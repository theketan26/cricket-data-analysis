with open("./process/all_json/README.txt", 'r') as all_json:
    all_json_data = all_json.read()

    all_json_data = all_json_data.split("\n")
    all_json_data = filter(lambda x: x[0] == '2' if len(x) > 0 else False, all_json_data)
    all_json_data = list(all_json_data)

    teams = set()

    for line_data in all_json_data:
        json_data = line_data.split(" - ")
        vss = json_data[5]
        teams_ = vss.split(" vs ")
        teams.add(teams_[0])
        teams.add(teams_[1])

    print(teams)