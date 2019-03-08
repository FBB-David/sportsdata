import json
from sportsdata.source.nba.scoreboard import Scoreboard
from sportsdata.source.nba.boxscore import BoxScore

class ResponseParser(object):
    pass

    @staticmethod
    def boxscore_player_track(response):
        boxscore = BoxScore()
        info = json.loads(response.text)
        for rs in info['resultSets']:
            if rs['name'] == 'PlayerStats':
                for row in rs['rowSet']:
                    player = dict(zip([h.lower() for h in rs['headers']], row))
                    hours, seconds = player['min'].split(':')
                    player['seconds_played'] = int(hours) * 60 + int(seconds)
                    boxscore.players.append(player)
            elif rs['name'] == 'TeamStats':
                for row in rs['rowSet']:
                    team = dict(zip([h.lower() for h in rs['headers']], row))
                    boxscore.teams.append(team)
            else:
                print(rs)
                pass
        return boxscore


    @staticmethod
    def scoreboard_v2(response):
        scoreboard  = Scoreboard()
        info        = json.loads(response.text)
        processed_games = []


        for rs in info['resultSets']:
            if rs['name'] == 'LineScore':
                for row in rs['rowSet']:
                    game = dict(zip([h.lower() for h in rs['headers']], row))
                    if game['game_id'] not in processed_games:
                        scoreboard.games.append(game)
                        processed_games.append(game['game_id'])
            elif rs['name'] == 'SeriesStandings':
                for row in rs['rowSet']:
                    info = dict(zip([h.lower() for h in rs['headers']], row))
                    scoreboard.series_standings.append(info)
            else:
                #print(rs)
                pass

        return scoreboard