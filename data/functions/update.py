from ..models import Matches


'''
updateMatches()
'''


'''

This function update match data from readme.txt file to django sqlite databse

'''
def updateMatches():
    file = open('data/json/README.txt', 'r')

    lines = file.readlines()
    size, n = len(lines), 1

    for line in lines:
        try:
            temp = list(map(lambda x: x.strip(), line[:-1].split("-")))
            data = {
                'date': '-'.join(temp[:3]),
                'base_type': temp[3],
                'type': temp[4],
                'gender': temp[5],
                'match_id': temp[6],
                'teams': temp[7]
            }
            if data['match_id'][0] == 'w':
                match = None
            else:
                try:
                    match = Matches(date=data['date'], base_type=data['base_type'], type=data['type'], gender=data['gender'], match_id=data['match_id'], teams=data['teams'])
                except:
                    match = None

            if match:
                print(n, '/', size)
                match.save()
        except:
            continue
        n += 1