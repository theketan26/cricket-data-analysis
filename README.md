# Cricket Data Analysis

install required packages

rm db.sqlite3

python manage.py migrate

python extract_json.py

python manage.py update_matches

python manage.py extract_teams

python manage.py clean_matches

python manage.py transform_players ODI
python manage.py transform_players Test
python manage.py transform_players T20

python manage.py runserver
