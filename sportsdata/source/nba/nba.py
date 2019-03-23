import requests
import requests_cache
import logging
import json

from sportsdata.source.nba.response_parser import ResponseParser
requests_cache.install_cache('sportsdata', expire_after=60*60*6) #Cache for 6 hours

class NBA:

    base_url = "http://stats.nba.com/stats/{0}"
    headers = {
        'user-agent': (
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),# noqa: E501
            'Dnt': ('1'),
            'Accept-Encoding': ('gzip, deflate, sdch'),
            'Accept-Language': ('en'),
            'origin': ('http://stats.nba.com')
    }
    league_ids = {'nba':'00','aba':'01'}

    def all_star_ballot_predictor(self, west_players, east_players, game_id, start, end):
        url = self.base_url.format("allstarballotpredictor")
        params = {'WestPlayer1': west_players[0], 'WestPlayer2': west_players[1],
                  'WestPlayer3': west_players[2], 'WestPlayer4': west_players[3],
                  'WestPlayer5': west_players[4], 'EastPlayer1': east_players[0],
                  'EastPlayer2': east_players[1], 'EastPlayer3': east_players[2],
                  'EastPlayer4': east_players[3], 'EastPlayer5': east_players[4],
                  'GameID':game_id, 'StartPeriod':start, 'EndPeriod':end
                  }

        logging.debug(url)
        req = requests.get(url,headers=self.headers)
        print(req.text)

    def boxscore_advanced(self, game_id, start_period, end_period, start_range, end_range, range_type):

        url = self.base_url.format("boxscoreadvancedv2")
        logging.info("Scoreboard URL: {0}".format(url))

        params = {'GameID':game_id,'StartPeriod':start_period,'EndPeriod':end_period,'StartRange':start_range,'EndRange':end_range,'RangeType':range_type}
        req = requests.get(url, headers=self.headers, params=params)
        print(url)
        print(req.text)
        data = json.loads(req.text)
        return data

    def boxscorefourfactorsv2(self):
        url = self.base_url.format("boxscorefourfactorsv2")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def boxscore_misc(self,game_id, start_period, end_period, start_range, end_range, range_type):
        params = {
            'GameID'        :   game_id,
            'StartPeriod'   :   start_period,
            'EndPeriod'     :   end_period,
            'StartRange'    :   start_range,
            'EndRange'      :   end_range,
            'RangeType'     :   range_type
        }
        url = self.base_url.format("boxscoremiscv2")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    def boxscore_player_track(self, game_id):
        url = self.base_url.format("boxscoreplayertrackv2")
        params  = {'GameID': game_id}
        req     = requests.get(url, headers=self.headers, params=params)
        data    = ResponseParser.boxscore_player_track(req)
        return data

    def boxscore_scoring(self, game_id, start_period, end_period, start_range, end_range, range_type):
        """

        Args:
            game_id: Identifier for the given Game
            start_period:
            end_period:
            start_range:
            end_range:
            range_type:

        Returns:

        """

        url     = self.base_url.format("boxscorescoringv2")
        params  = {'GameID'         :   game_id         ,
                   'StartPeriod'    :   start_period    ,   'EndPeriod' :   end_period,
                   'StartRange'     :   start_range     ,   'EndRange'  :   end_range, 'RangeType'  :   range_type}
        req     = requests.get(url, headers=self.headers, params=params)
        print(req.text)
        data    = json.loads(req.text)
        return data

    def boxscore_summary(self, game_id):
        url     = self.base_url.format("boxscoresummaryv2")
        params  = {'GameID' : game_id}
        resp    = requests.get(url, headers=self.headers, params=params)
        data    = ResponseParser.boxscore_summary(resp)
        return data

    def boxscore_traditional(self, game_id, start_period, end_period, start_range, end_range, range_type):
        params = {
            'GameID'        :   game_id,
            'StartPeriod'   :   start_period,
            'EndPeriod'     :   end_period,
            'StartRange'    :   start_range,
            'EndRange'      :   end_range,
            'RangeType'     :   range_type
        }
        url = self.base_url.format("boxscoretraditionalv2")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    def boxscore_usage(self, game_id, start_period, end_period, start_range, end_range, range_type):
        params = {
            'GameID': game_id,
            'StartPeriod': start_period,
            'EndPeriod': end_period,
            'StartRange': start_range,
            'EndRange': end_range,
            'RangeType': range_type
        }
        url = self.base_url.format("boxscoreusagev2")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def common_team_years(self, league_id):
        """
        Retrieves a list of all starting/ending year for each team
        Args:
            league_id:

        Returns:

        """
        params = {'LeagueID':league_id}
        url = self.base_url.format("commonTeamYears")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    def common_all_players(self, league_id, season, is_only_current_season):
        params = {
            'LeagueID' : league_id ,
            'Season' : season ,
            'IsOnlyCurrentSeason' : is_only_current_season
        }
        url = self.base_url.format("commonallplayers")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    def common_player_info(self, player_id):
        params = {
            'PlayerID':player_id
        }
        url = self.base_url.format("commonplayerinfo")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    def commonplayoffseries(self):
        url = self.base_url.format("commonplayoffseries")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def commonteamroster(self):
        url = self.base_url.format("commonteamroster")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url,headers=self.headers)
        print(req.text)

    def draftcombinedrillresults(self):
        url = self.base_url.format("draftcombinedrillresults")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def draftcombinenonstationaryshooting(self):
        url = self.base_url.format("draftcombinenonstationaryshooting")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def draftcombineplayeranthro(self):
        url = self.base_url.format("draftcombineplayeranthro")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def draftcombinespotshooting(self):
        url = self.base_url.format("draftcombinespotshooting")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def draftcombinestats(self):
        url = self.base_url.format("draftcombinestats")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def drafthistory(self):
        url = self.base_url.format("drafthistory")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def franchisehistory(self):
        url = self.base_url.format("franchisehistory")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def homepageleaders(self):
        url = self.base_url.format("homepageleaders")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def homepagev2(self):
        url = self.base_url.format("homepagev2")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaderstiles(self):
        url = self.base_url.format("leaderstiles")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashlineups(self):
        url = self.base_url.format("leaguedashlineups")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashplayerbiostats(self):
        url = self.base_url.format("leaguedashplayerbiostats")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashplayerclutch(self):
        url = self.base_url.format("leaguedashplayerclutch")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashplayerptshot(self):
        url = self.base_url.format("leaguedashplayerptshot")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashplayershotlocations(self):
        url = self.base_url.format("leaguedashplayershotlocations")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashplayerstats(self):
        url = self.base_url.format("leaguedashplayerstats")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashptdefend(self):
        url = self.base_url.format("leaguedashptdefend")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashteamclutch(self):
        url = self.base_url.format("leaguedashteamclutch")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashteamptshot(self):
        url = self.base_url.format("leaguedashteamclutch")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashteamshotlocations(self):
        url = self.base_url.format("leaguedashteamclutch")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashteamstats(self):
        url = self.base_url.format("leaguedashteamstats")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leagueleaders(self):
        url = self.base_url.format("leaguedashteamstats")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def play_by_play(self, game_id, start_period, end_period, returnResponse=False):
        """
        playbyplay endpoint

        Args:
            game_id:
            start_period: ???
            end_period: ???
            returnResponse: Controls whether processed data or the unprocessed response is returned

        Returns:

        """
        url = self.base_url.format("playbyplay")
        logging.debug("Scoreboard URL: {0}".format(url))
        print("Scoreboard URL: {0}".format(url))
        params = {'GameID':game_id,'StartPeriod':start_period,'EndPeriod':end_period}
        resp = requests.get(url, headers=self.headers,params=params)
        print(resp.text)
        if (returnResponse):
            return resp

        data = json.loads(resp.text)
        return data

    def playbyplayv2(self):
        url = self.base_url.format("playbyplayv2")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playercareerstats(self):
        url = self.base_url.format("playbyplayv2")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playercompare(self):
        url = self.base_url.format("playbyplayv2")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbyclutch(self):
        url = self.base_url.format("playerdashboardbyclutch")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbygamesplits(self):
        url = self.base_url.format("playerdashboardbygamesplits")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbygeneralsplits(self):
        url = self.base_url.format("playerdashboardbygeneralsplits")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbylastngames(self):
        url = self.base_url.format("playerdashboardbylastngames")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbyopponent(self):
        url = self.base_url.format("playerdashboardbyopponent")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbyshootingsplits(self):
        url = self.base_url.format("playerdashboardbyshootingsplits")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbyteamperformance(self):
        url = self.base_url.format("playerdashboardbyteamperformance")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbyyearoveryear(self):
        url = self.base_url.format("playerdashboardbyyearoveryear")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashptpass(self):
        url = self.base_url.format("playerdashptpass")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashptreb(self):
        url = self.base_url.format("playerdashptreb")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashptshotdefend(self):
        url = self.base_url.format("playerdashptshotdefend")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashptshots(self):
        url = self.base_url.format("playerdashptshots")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playergamelog(self):
        url = self.base_url.format("playergamelog")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerprofile(self):
        url = self.base_url.format("playerprofile")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerprofilev2(self):
        url = self.base_url.format("playerprofilev2")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playersvsplayers(self):
        url = self.base_url.format("playersvsplayers")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playervsplayer(self):
        url = self.base_url.format("playervsplayer")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playoff_picture(self, league_id, season_id):
        """

        Args:
            league_id:
            season_id:

        Returns:

        """
        params  =   {
            'LeagueID' : league_id ,
            'SeasonID' : season_id
        }
        url = self.base_url.format("playoffpicture")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    def scoreboard(self,game_date, leauge_id, day_offset):
        url = self.base_url.format("scoreboard")
        logging.debug("Scoreboard URL: {0}".format(url))
        params = {'GameDate':game_date, 'LeagueID':leauge_id, 'DayOffset':day_offset}
        req = requests.get(url,headers=self.headers,params=params)
        data = json.loads(req.text)
        return data

    def scoreboard_v2(self,game_date, leauge_id, day_offset):
        url     = self.base_url.format("scoreboardv2")
        params  = {'GameDate':game_date,'LeagueID':leauge_id,'DayOffset':day_offset}
        req     = requests.get(url,headers=self.headers,params=params)
        data    = ResponseParser.scoreboard_v2(req)

        return data

    def shot_chart_detail(self, season_type, team_id, player_id, game_id,outcome, location, month, season_segment,
                          date_from, date_to, opponent_team_id, vs_conference, vs_division, player_position, rookie_year,
                          game_segment, period, last_n_games, context_measure):
        params  =   {
            'SeasonType'        : season_type    ,
            'TeamID'            : team_id    ,
            'PlayerID'          : player_id  ,
            'GameID'            : game_id ,
            'Outcome'           : outcome           ,
            'Location'          : location          ,
            'Month'             : month             ,
            'SeasonSegment'     : season_segment    ,
            'DateFrom'          : date_from,
            'DateTo'            : date_to   ,
            'OpponentTeamID'    : opponent_team_id ,
            'VsConference'      : vs_conference ,
            'VsDivision'        : vs_division ,
            'PlayerPosition'    : player_position ,
            'RookieYear'        : rookie_year ,
            'GameSegment'       : game_segment,
            'Period'            : period ,
            'LastNGames'        : last_n_games ,
            'ContextMeasure'    : context_measure
        }

        url = self.base_url.format("shotchartdetail")
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    def shotchartlineupdetail(self):
        url = self.base_url.format("shotchartlineupdetail")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbyclutch(self):
        url = self.base_url.format("teamdashboardbyclutch")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbygamesplits(self):
        url = self.base_url.format("teamdashboardbygamesplits")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbygeneralsplits(self):
        url = self.base_url.format("teamdashboardbygeneralsplits")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbylastngames(self):
        url = self.base_url.format("teamdashboardbylastngames")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbyopponent(self):
        url = self.base_url.format("teamdashboardbyopponent")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbyshootingsplits(self):
        url = self.base_url.format("teamdashboardbyshootingsplits")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbyteamperformance(self):
        url = self.base_url.format("teamdashboardbyteamperformance")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbyyearoveryear(self):
        url = self.base_url.format("teamdashboardbyyearoveryear")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashlineups(self):
        url = self.base_url.format("teamdashlineups")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashptpass(self):
        url = self.base_url.format("teamdashptpass")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashptreb(self):
        url = self.base_url.format("teamdashptreb")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashptshots(self):
        url = self.base_url.format("teamdashptshots")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamgamelog(self):
        url = self.base_url.format("teamgamelog")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teaminfocommon(self):
        url = self.base_url.format("teaminfocommon")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamplayerdashboard(self):
        url = self.base_url.format("teamplayerdashboard")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamplayeronoffdetails(self):
        url = self.base_url.format("teamplayeronoffdetails")
        req = requests.get(url, headers=self.headers)
        print(req.text)


    def team_player_on_off_summary(self, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season_type,
                                   outcome, location, month, season_segment, date_from , date_to, opponent_team_id,
                                   vs_conference, vs_division, game_segment, period, last_n_games):
        """

        Returns:


        """

        params  =   {
                    'TeamID'            : team_id           ,
                    'MeasureType'       : measure_type      ,
                    'PerMode'           : per_mode          ,
                    'PlusMinus'         : plus_minus        ,
                    'PaceAdjust'        : pace_adjust       ,
                    'Rank'              : rank              ,
                    'SeasonType'        : season_type       ,
                    'Outcome'           : outcome           ,
                    'Location'          : location          ,
                    'Month'             : month             ,
                    'SeasonSegment'     : season_segment    ,
                    'DateFrom'          : date_from         ,
                    'DateTo'            : date_to           ,
                    'OpponentTeamID'    : opponent_team_id  ,
                    'VsConference'      : vs_conference     ,
                    'VsDivision'        : vs_division       ,
                    'GameSegment'       : game_segment      ,
                    'Period'            : period            ,
                    'LastNGames'        : last_n_games
        }
        url = self.base_url.format("teamplayeronoffsummary")
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)


    def team_vs_player(self):
        url = self.base_url.format("teamvsplayer")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def team_year_by_years(self, league_id, season_type, per_mode, team_id):
        params  =   {'LeagueID'     :   league_id,
                     'SeasonType'   :   season_type,
                     'PerMode'      :   per_mode    ,
                     'TeamID'       :   team_id
                     }
        url = self.base_url.format("teamyearbyyearstats")
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    def video_status(self,game_date, league_id):
        """

        Args:
            game_date:
            league_id:

        Returns:

        """
        params  =   {'LeagueID' :   league_id,
                     'GameDate' :   game_date}
        url = self.base_url.format("videoStatus")
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)