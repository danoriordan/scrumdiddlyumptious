

##### Begin of get_league_standing #####

import requests
import json

def get_league_standings(api_key='b64cf203e1344da7aa05e8bd29bba0f9'):
    url = "http://api.football-data.org/v4/competitions/PL/standings"
    headers = {"X-Auth-Token": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()

    standings = []  

    if 'standings' in data:
        for standing in data['standings']:
            if standing['type'] == 'TOTAL':  
                for team in standing['table']:
                    team_data = {
                        "position": team['position'],
                        "teamName": team['team']['name'],
                        "playedGames": team['playedGames'],
                        "won": team['won'],
                        "draw": team['draw'],
                        "lost": team['lost'],
                        "points": team['points'],
                        "goalsFor": team['goalsFor'],
                        "goalsAgainst": team['goalsAgainst'],
                        "goalDifference": team['goalDifference']
                    }
                    standings.append(team_data)
                break  

        standings_json = json.dumps(standings, ensure_ascii=False, indent=4)
        return standings_json
    else:
        return "Error"

#### End of get_league_standing ####

        