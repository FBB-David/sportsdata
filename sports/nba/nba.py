from .constants import *
from enum       import Enum
from inspect    import isclass

import requests
import requests_cache
import logging
import json

from sports.source.nba.response_parser import ResponseParser
requests_cache.install_cache('sports', expire_after=60*60*6) #Cache for 6 hours


def clean_inputs(func):
    def new_func(*args,**kwargs):
        cleaned_args = []
        for i in range(len(args)):
            if isclass(type(args[i])) and issubclass(type(args[i]),Enum):
                clean_arg = args[i].value
                cleaned_args.append(clean_arg)
            else:
                cleaned_args.append(args[i])


        #print(**kwargs)
        for key, val in kwargs.items():
            print(key)
        data = func(*cleaned_args,*kwargs)
        return data
    return new_func


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

    @clean_inputs
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

    @clean_inputs
    def boxscore_advanced(self, game_id, start_period, end_period, start_range, end_range, range_type):

        url = self.base_url.format("boxscoreadvancedv2")
        logging.info("Scoreboard URL: {0}".format(url))

        params = {'GameID':game_id,'StartPeriod':start_period,'EndPeriod':end_period,'StartRange':start_range,'EndRange':end_range,'RangeType':range_type}
        req = requests.get(url, headers=self.headers, params=params)
        print(url)
        print(req.text)
        data = json.loads(req.text)
        return data

    @clean_inputs
    def boxscore_four_factors(self,game_id, start_period, end_period, start_range, end_range, range_type):
        params = {
            'GameID'        :   game_id,
            'StartPeriod'   :   start_period,
            'EndPeriod'     :   end_period,
            'StartRange'    :   start_range,
            'EndRange'      :   end_range,
            'RangeType'     :   range_type
        }
        url = self.base_url.format("boxscorefourfactorsv2")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
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

    @clean_inputs
    def boxscore_player_track(self, game_id):
        url = self.base_url.format("boxscoreplayertrackv2")
        params  = {'GameID': game_id}
        req     = requests.get(url, headers=self.headers, params=params)
        data    = ResponseParser.boxscore_player_track(req)
        return data

    @clean_inputs
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

    @clean_inputs
    def boxscore_summary(self, game_id):
        url     = self.base_url.format("boxscoresummaryv2")
        params  = {'GameID' : game_id}
        resp    = requests.get(url, headers=self.headers, params=params)
        data    = ResponseParser.boxscore_summary(resp)
        return data

    @clean_inputs
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

    @clean_inputs
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

    @clean_inputs
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

    @clean_inputs
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

    @clean_inputs
    def common_player_info(self, player_id):
        params = {
            'PlayerID':player_id
        }
        url = self.base_url.format("commonplayerinfo")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def common_playoff_series(self, league_id, season):
        params = {
            'LeagueID' : league_id ,
            'Season' : season
        }
        url = self.base_url.format("commonplayoffseries")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def common_team_roster(self, season, team_id):
        params = {
            'TeamID' : team_id ,
            'Season' : season
        }
        url = self.base_url.format("commonteamroster")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url,headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def draft_combine_drill_results(self, league_id, season):
        params = {
            'LeagueID'      : league_id,
            'SeasonYear'    : season
        }
        url = self.base_url.format("draftcombinedrillresults")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def draft_combine_non_stationary_shooting(self, league_id, season):
        params = {
            'LeagueID': league_id,
            'SeasonYear': season
        }
        url = self.base_url.format("draftcombinenonstationaryshooting")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def draft_combine_player_anthro(self, league_id, season):
        params = {
            'LeagueID': league_id,
            'SeasonYear': season
        }
        url = self.base_url.format("draftcombineplayeranthro")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def draft_combine_spot_shooting(self, league_id, season):
        params = {
            'LeagueID': league_id,
            'SeasonYear': season
        }
        url = self.base_url.format("draftcombinespotshooting")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def draft_combine_stats(self):
        url = self.base_url.format("draftcombinestats")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def draft_history(self, league_id):
        params = {
            'LeagueID': league_id,
        }
        url = self.base_url.format("drafthistory")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def franchise_history(self, league_id):
        params = {
            'LeagueID': league_id,
        }
        url = self.base_url.format("franchisehistory")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def homepage_leaders(self, stat_category, league_id, season, season_type, player_or_team, game_scope, player_scope):
        params = {
            'StatCategory'  : stat_category ,
            'LeagueID'      : league_id,
            'Season'        : season ,
            'SeasonType'    : season_type ,
            'PlayerOrTeam'  : player_or_team ,
            'Game Scope'    : game_scope ,
            'Player Scope'  : player_scope
        }
        url = self.base_url.format("homepageleaders")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def homepage(self, stat_category, league_id, season, season_type, player_or_team, game_scope, player_scope):
        params = {
            'StatCategory'  : stat_category     ,
            'LeagueID'      : league_id         ,
            'Season'        : season            ,
            'SeasonType'    : season_type       ,
            'PlayerOrTeam'  : player_or_team    ,
            'Game Scope'    : game_scope        ,
            'Player Scope'  : player_scope
        }
        url = self.base_url.format("homepagev2")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def leaderstiles(self, stat_category, league_id, season, season_type, player_or_team, game_scope, player_scope):
        params = {
            'StatCategory'  : stat_category     ,
            'LeagueID'      : league_id         ,
            'Season'        : season            ,
            'SeasonType'    : season_type       ,
            'PlayerOrTeam'  : player_or_team    ,
            'Game Scope'    : game_scope        ,
            'Player Scope'  : player_scope
        }

        url = self.base_url.format("leaderstiles")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def league_dash_lineups(self, group_quantity, season_type, measure_type, per_mode, plus_minus, pace_adjust, rank,
                            outcome,location, month, season_segment, date_from):
        params = {
            'GroupQuantity'     : group_quantity,
            'SeasonType'        : season_type,
            'MeasureType'       : measure_type,
            'PerMode'           : per_mode,
            'PlusMinus'         : plus_minus,
            'PaceAdjust'        : pace_adjust,
            'Rank'              : rank,
            'Outcome':outcome,
            'Location':location,
            'Month':month,
            'SeasonSegment':season_segment,
            'DateFrom':date_from
        }
        url = self.base_url.format("leaguedashlineups")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def leaguedashplayerbiostats(self):
        url = self.base_url.format("leaguedashplayerbiostats")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def leaguedashplayerclutch(self):
        url = self.base_url.format("leaguedashplayerclutch")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def leaguedashplayerptshot(self):
        url = self.base_url.format("leaguedashplayerptshot")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def leaguedashplayershotlocations(self):
        url = self.base_url.format("leaguedashplayershotlocations")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def leaguedashplayerstats(self):
        url = self.base_url.format("leaguedashplayerstats")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def leaguedashptdefend(self):
        url = self.base_url.format("leaguedashptdefend")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def leaguedashteamclutch(self):
        url = self.base_url.format("leaguedashteamclutch")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def leaguedashteamptshot(self):
        url = self.base_url.format("leaguedashteamclutch")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def leaguedashteamshotlocations(self):
        url = self.base_url.format("leaguedashteamclutch")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def leaguedashteamstats(self):
        url = self.base_url.format("leaguedashteamstats")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def league_leaders(self, measure_type, per_mode, plus_minus, pace_adjust, rank, season_type, outcome):
        params = {
            'MeasureType' : measure_type,
            'PerMode'       : per_mode    ,
            'PlusMinus'     : plus_minus    ,
            'PaceAdjust'    : pace_adjust,
            'Rank'          : rank,
            'SeasonType'    : season_type,
            'Outcome'       : outcome,

        }
        url = self.base_url.format("leaguedashteamstats")
        logging.debug("Requesting data from '{0}'".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
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
        print("Requesting data from '{0}'".format(url))
        params = {'GameID':game_id,'StartPeriod':start_period,'EndPeriod':end_period}
        resp = requests.get(url, headers=self.headers,params=params)
        print(resp.text)
        if (returnResponse):
            return resp

        data = json.loads(resp.text)
        return data

    @clean_inputs
    def playbyplayv2(self):
        url = self.base_url.format("playbyplayv2")
        logging.debug("Requesting data from '{0}'".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playercareerstats(self):
        url = self.base_url.format("playbyplayv2")
        logging.debug("Requesting data from '{0}'".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playercompare(self):
        url = self.base_url.format("playbyplayv2")
        logging.debug("Requesting data from '{0}'".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playerdashboardbyclutch(self):
        url = self.base_url.format("playerdashboardbyclutch")
        logging.debug("Requesting data from '{0}'".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playerdashboardbygamesplits(self):
        url = self.base_url.format("playerdashboardbygamesplits")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playerdashboardbygeneralsplits(self):
        url = self.base_url.format("playerdashboardbygeneralsplits")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playerdashboardbylastngames(self):
        url = self.base_url.format("playerdashboardbylastngames")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playerdashboardbyopponent(self):
        url = self.base_url.format("playerdashboardbyopponent")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def player_dashboard_by_shooting_splits(self, measure_type, per_mode, plus_minus, pace_adjust,rank, season_type,
                                            player_id, outcome, location, month, season_segment, date_from,
                                            date_to, opponent_team_id, vs_conference, period,
                                            last_n_games,
                                            vs_division=Division.ALL.value,
                                            game_segment=GameSegment.FULL_GAME.value):
        params = {
            'MeasureType'   : measure_type      ,
            'PerMode'       : per_mode          ,
            'PlusMinus'     : plus_minus        ,
            'PaceAdjust'    : pace_adjust       ,
            'Rank'          : rank              ,
            'SeasonType'    : season_type       ,
            'PlayerID'      : player_id         ,
            'Outcome'       : outcome           ,
            'Location'      : location          ,
            'Month'         : month             ,
            'SeasonSegment' : season_segment    ,
            'DateFrom'      : date_from         ,
            'DateTo'        : date_to           ,
            'OpponentTeamID':opponent_team_id   ,
            'VsConference'  : vs_conference     ,
            'VsDivision'    : vs_division       ,
            'GameSegment'   : game_segment      ,
            'Period'        : period            ,
            'LastNGames'    : last_n_games
        }
        url = self.base_url.format("playerdashboardbyshootingsplits")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def player_dashboard_by_team_performance(self, measure_type, per_mode, plus_minus, pace_adjust,rank, season_type,
                                            player_id, outcome, location, month, season_segment, date_from,
                                            date_to, opponent_team_id, vs_conference, period, last_n_games,
                                             vs_division=Division.ALL.value,
                                             game_segment=''):
        params = {
            'MeasureType'       : measure_type  ,
            'PerMode'           : per_mode      ,
            'PlusMinus'         : plus_minus    ,
            'PaceAdjust'        : pace_adjust   ,
            'Rank'              : rank          ,
            'SeasonType'        : season_type   ,
            'PlayerID'          : player_id     ,
            'Outcome'           : outcome       ,
            'Location'          : location      ,
            'Month'             : month         ,
            'SeasonSegment'     : season_segment,
            'DateFrom'          : date_from     ,
            'DateTo'            : date_to       ,
            'OpponentTeamID'    : opponent_team_id,
            'VsConference'      : vs_conference ,
            'VsDivision'        : vs_division   ,
            'GameSegment'       : game_segment  ,
            'Period'            : period        ,
            'LastNGames'        : last_n_games
        }
        url = self.base_url.format("playerdashboardbyteamperformance")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def playerdashboardbyyearoveryear(self):
        url = self.base_url.format("playerdashboardbyyearoveryear")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playerdashptpass(self):
        url = self.base_url.format("playerdashptpass")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playerdashptreb(self):
        url = self.base_url.format("playerdashptreb")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playerdashptshotdefend(self):
        url = self.base_url.format("playerdashptshotdefend")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playerdashptshots(self):
        url = self.base_url.format("playerdashptshots")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playergamelog(self):
        url = self.base_url.format("playergamelog")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playerprofile(self):
        url = self.base_url.format("playerprofile")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playerprofilev2(self):
        url = self.base_url.format("playerprofilev2")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playersvsplayers(self):
        url = self.base_url.format("playersvsplayers")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def playervsplayer(self):
        url = self.base_url.format("playervsplayer")
        logging.debug("Scoreboard URL: {0}".format(url))
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
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

    @clean_inputs
    def scoreboard(self, game_date, league_id, day_offset):
        url = self.base_url.format("scoreboard")
        logging.debug("Scoreboard URL: {0}".format(url))
        params = {'GameDate':game_date, 'LeagueID':league_id, 'DayOffset':day_offset}
        req = requests.get(url,headers=self.headers,params=params)
        data = json.loads(req.text)
        return data

    @clean_inputs
    def scoreboard_v2(self,game_date, leauge_id, day_offset):
        url     = self.base_url.format("scoreboardv2")
        params  = {'GameDate':game_date,'LeagueID':leauge_id,'DayOffset':day_offset}
        req     = requests.get(url,headers=self.headers,params=params)
        data    = ResponseParser.scoreboard_v2(req)

        return data

    @clean_inputs
    def shot_chart_detail(self, season_type, team_id, player_id, game_id,outcome, location, month, season_segment,
                          date_from, date_to, opponent_team_id,
                          player_position, rookie_year,
                          period, last_n_games, context_measure,
                          vs_conference=Conference.ALL.value,
                          vs_division=Division.ALL.value,
                          game_segment=GameSegment.FULL_GAME.value):
        params  =   {
            'SeasonType'        : season_type       ,
            'TeamID'            : team_id           ,
            'PlayerID'          : player_id         ,
            'GameID'            : game_id           ,
            'Outcome'           : outcome           ,
            'Location'          : location          ,
            'Month'             : month             ,
            'SeasonSegment'     : season_segment    ,
            'DateFrom'          : date_from         ,
            'DateTo'            : date_to           ,
            'OpponentTeamID'    : opponent_team_id  ,
            'VsConference'      : vs_conference     ,
            'VsDivision'        : vs_division       ,
            'PlayerPosition'    : player_position   ,
            'RookieYear'        : rookie_year       ,
            'GameSegment'       : game_segment      ,
            'Period'            : period            ,
            'LastNGames'        : last_n_games      ,
            'ContextMeasure'    : context_measure
        }

        url = self.base_url.format("shotchartdetail")
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def shot_chart_lineup_detail(self, league_id, season, season_type, team_id, outcome, location, month, season_segment):
        params = {
            'LeagueID'      :   league_id,
            'Season'        :   season,
            'SeasonType'    :   season_type,
            'TeamID'        :   team_id,
            'Outcome'       :   outcome,
            'Location'      :   location,
            'Month'         :   month,
            'SeasonSegment' :   season_segment
        }

        url = self.base_url.format("shotchartlineupdetail")
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def teamdashboardbyclutch(self):
        url = self.base_url.format("teamdashboardbyclutch")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def teamdashboardbygamesplits(self):
        url = self.base_url.format("teamdashboardbygamesplits")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def teamdashboardbygeneralsplits(self):
        url = self.base_url.format("teamdashboardbygeneralsplits")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def teamdashboardbylastngames(self):
        url = self.base_url.format("teamdashboardbylastngames")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def teamdashboardbyopponent(self):
        url = self.base_url.format("teamdashboardbyopponent")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def teamdashboardbyshootingsplits(self):
        url = self.base_url.format("teamdashboardbyshootingsplits")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def teamdashboardbyteamperformance(self):
        url = self.base_url.format("teamdashboardbyteamperformance")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def team_dashboard_by_year_over_year(self, team_id, per_mode, season_type, month, outcome, location,
                                         season_segment, date_from, date_to):
        params  =   {
            'TeamID'        : team_id,
            'PerMode'       : per_mode,
            'SeasonType'    : season_type,
            'Month'         : month,
            'Outcome'       : outcome,
            'Location'      : location,
            'SeasonSegment' : season_segment,
            'DateFrom'      : date_from,
            'DateTo'        :   date_to
        }
        url = self.base_url.format("teamdashboardbyyearoveryear")
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def team_dash_lineups(self):
        url = self.base_url.format("teamdashlineups")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def team_dash_pt_pass(self):
        url = self.base_url.format("teamdashptpass")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def team_dash_pt_reb(self):
        url = self.base_url.format("teamdashptreb")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def team_dash_pt_shots(self, per_mode, season, season_type, team_id, outcome, location, month, season_segment,
                           date_from, date_to, opponent_team_id, period, last_n_games,
                           vs_division=Division.ALL.value,
                           vs_conference=Conference.ALL.value,
                           game_segment=GameSegment.FULL_GAME.value):
        params = {
            'PerMode'           : per_mode,
            'Season'            : season,
            'SeasonType'        : season_type,
            'TeamID'            : team_id,
            'Outcome'           : outcome,
            'Location'          : location,
            'Month'             : month,
            'SeasonSegment'     : season_segment,
            'DateFrom'          : date_from,
            'DateTo'            : date_to,
            'OpponentTeamID'    : opponent_team_id,
            'VsConference'      : vs_conference,
            'VsDivision'        : vs_division,
            'GameSegment'       : game_segment,
            'Period'            : period,
            'LastNGames'        : last_n_games
        }
        url = self.base_url.format("teamdashptshots")
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def team_game_log(self, team_id, season, season_type):
        params = {
            'TeamID'        : team_id       ,
            'Season'        : season        ,
            'SeasonType'    : season_type
        }
        url = self.base_url.format("teamgamelog")
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def team_info_common(self, league_id, team_id):
        params = {
            'LeagueID'  : league_id ,
            'TeamID'    : team_id
        }

        url     = self.base_url.format("teaminfocommon")
        req     = requests.get(url, headers=self.headers, params=params)
        data    = ResponseParser.get_dataframes(req)
        return data

    @clean_inputs
    def team_player_dashboard(self):
        url = self.base_url.format("teamplayerdashboard")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def team_player_on_off_details(self):
        url = self.base_url.format("teamplayeronoffdetails")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    @clean_inputs
    def team_player_on_off_summary(self, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season_type,
                                   outcome, location, month, season_segment, date_from , date_to, opponent_team_id,
                                   vs_conference, period, last_n_games,
                                   vs_division=Division.ALL.value,
                                   game_segment=GameSegment.FULL_GAME.value):
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

    @clean_inputs
    def team_vs_player(self,team_id, vs_player_id):
        params = {
            'TeamID'            : team_id           ,
            'VsPlayerID'        : vs_player_id      ,
        }
        url = self.base_url.format("teamvsplayer")
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
    def team_year_by_years(self, league_id, season_type, per_mode, team_id):
        params  =   {'LeagueID'     :   league_id,
                     'SeasonType'   :   season_type,
                     'PerMode'      :   per_mode    ,
                     'TeamID'       :   team_id
                     }
        url = self.base_url.format("teamyearbyyearstats")
        req = requests.get(url, headers=self.headers, params=params)
        print(req.text)

    @clean_inputs
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