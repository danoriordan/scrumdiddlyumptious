import json
from skills import get_league_standings

def find_team_data(team_name, standings):
    for team in standings:
        if team['teamName'] == team_name:
            return team
    return None

# Retrieve the current standings for the English Premier League
epl_standings_json = get_league_standings()
epl_standings = json.loads(epl_standings_json)

# Find Manchester United's data
man_utd = find_team_data('Manchester United', epl_standings)
if man_utd:
    man_utd_wins = man_utd.get('won')
    man_utd_losses = man_utd.get('lost')
    print("Manchester United's wins:", man_utd_wins)
    print("Manchester United's losses:", man_utd_losses)
else:
    print("Manchester United's data not found in the standings.")