import json
from sportsdata.source.nba.scoreboard import Scoreboard

class ResponseParser(object):
    pass

    @staticmethod
    def scoreboard_v2(response):
        scoreboard  = Scoreboard()
        info        = json.loads(response.text)

        for rs in info['resultSets']:
            if rs['name'] == 'LineScore':
                for row in rs['rowSet']:
                    game = dict(zip([h.lower() for h in rs['headers']], row))
                    scoreboard.games.append(game)
            elif rs['name'] == 'SeriesStandings':
                for row in rs['rowSet']:
                    info = dict(zip([h.lower() for h in rs['headers']], row))
                    scoreboard.series_standings.append(info)
            else:
                print(rs)

        return scoreboard