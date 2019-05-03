# Import all convenience enums and teams
from sports.nba.constants import *
from sports.nba.teams   import *

from sports.nba.api     import NBA
from datetime           import datetime



import pandas as pd


###############################
# Global Pandas Configuration #
###############################
pd.set_option('display.max_columns', None)

nba = NBA()



##########################################
# Get all Player Data for a given season #
##########################################
#players = nba.players(league_id=League.NBA, season='2014-15', is_only_current_season=0)
#print(players.keys())

####################################################################
# Get the Roster (Players and Coaches) for a Given Team and Season #
####################################################################
#frames = nba.team_roster(team_id=1610612739, season='2018-19')
#players = frames['players']
#coaches = frames['coaches']
#with pd.option_context('display.max_rows', 9999) and pd.option_context('display.max_columns',None):
#    print(players)
#    print(coaches)


########################
# Pandas Configuration #
########################
#pd.set_option('display.max_columns', None)

#games = nba.league_game_log(season='2018-19', player_or_team='P')
#print(games)

##########################
# API Endpoint Reference #
##########################
#nba.all_star_ballot_predictor()


#####################
# Logical Endpoints #
#####################

# Get all Player Data for a given season
#players = nba.players(league_id=League.NBA, season='2014-15', is_only_current_season=0)
#print(players.keys())

#team_id =
player_id = 203111

#nba.all_star_ballot_predictor()

today = datetime.today()
#nba.video_status(today, League.NBA.value)



#######################
# NBA Playoff Picture #
#######################
data = nba.playoff_picture(League.NBA.value,
                           season_id='22018')
for key, df in data.items():
    print(key)
    print(df)
#nba.shot_chart_detail()


#nba.common_all_players(League.NBA.value,season='2014-15',is_only_current_season=1)

#nba.common_player_info(203128)

#nba.common_team_years(League.NBA.value)

#nba.boxscore_traditional(game_id= , start_period=, end_period=, start_range=,end_range=, range_type=)

#nba.boxscore_usage(game_id= , start_period=, end_period=, start_range=,end_range=, range_type=)

#nba.boxscore_misc(game_id= , start_period=, end_period=, start_range=,end_range=, range_type=)


#nba.boxscore_four_factors()

#nba.common_playoff_series(league_id=League.NBA.value,season='2014-15')

#nba.common_team_roster(season='2013-14', team_id=1610612748)


#nba.draft_combine_drill_results(league_id=League.NBA.value, season='2017-18')

#nba.draft_combine_non_stationary_shooting(league_id=League.NBA.value, season='2017-18')

#nba.draft_combine_player_anthro(league_id=League.NBA.value, season='2017-18')

#nba.draft_combine_spot_shooting(league_id=League.NBA.value, season='2017-18')

#nba.draft_history(league_id=League.NBA.value)

#nba.franchise_history(league_id=League.NBA.value)

#nba.homepageleaders()

#nba.homepage()

#nba.leaderstiles()

#nba.leaguedashlineups()

#nba.league_leaders(measure_type=MeasureType.BASE.value, per_mode=PerMode.TOTALS.value, plus_minus='Y',
#                   pace_adjust='N', rank='N', season_type=SeasonType.REGULAR_SEASON.value, outcome=Outcome.WIN.value)



#nba.player_dashboard_by_shooting_splits(measure_type=MeasureType.BASE.value, per_mode=PerMode.MINUTE.value, plus_minus='Y',
#                                        pace_adjust='Y', rank='Y', season_type=SeasonType.PLAYOFFS.value, player_id=player_id,
#                                        outcome=Outcome.WIN.value, location=Location.ANYWHERE.value, month=6,
#                                        season_segment=SeasonSegment.FULL_SEASON.value,date_from=today,date_to=today,
#                                        opponent_team_id=1610612742, vs_conference='',vs_division='',
#                                        game_segment=GameSegment.FIRST_HALF.value, period=Period.ALL_PERIODS.value,
#                                        last_n_games=0)




#nba.player_dashboard_by_team_performance(measure_type=MeasureType.BASE.value, per_mode=PerMode.MINUTE.value, plus_minus='Y',
#                                        pace_adjust='Y', rank='Y', season_type=SeasonType.PLAYOFFS.value, player_id=player_id,
#                                        outcome=Outcome.WIN.value, location=Location.HOME.value, month=6,
#                                        season_segment=SeasonSegment.FULL_SEASON.value,date_from=today,date_to=today,
#                                        opponent_team_id=1610612742, vs_conference='',vs_division='',
#                                        game_segment=GameSegment.FIRST_HALF.value, period=Period.ALL_PERIODS.value,
#                                        last_n_games=0)



#data = nba.team_info_common(League.NBA, AtlantaHawks().team_id)
#print(data['TeamSeasonRanks'])

#nba.team_game_log(DenverNuggets().team_id, season='2018-19', season_type=SeasonType.REGULAR_SEASON.value)

#nba.team_dash_pt_shots(per_mode=PerMode.TOTALS.value, season='2016-17', season_type=SeasonType.REGULAR_SEASON.value,
#                       team_id=DenverNuggets().team_id, outcome=Outcome.WIN.value, location=Location.HOME,
#


#nba.team_dashboard_by_year_over_year()

#nba.shot_chart_lineup_detail(league_id=League.NBA.value, season='2015-16',season_type=SeasonType.REGULAR_SEASON.value,
#                             team_id=BostonCeltics().team_id, outcome=Outcome.LOSS.value, month=0,
#                             season_segment=SeasonSegment.FULL_SEASON.value, location=Location.HOME.value)


#nba.team_vs_player(DenverNuggets().team_id, player_id)

#nba.team_player_on_off_details(OklahomaThunder.team_id)