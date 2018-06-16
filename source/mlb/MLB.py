import chardet
import json
import xml
from urllib.request import urlopen
from sportsdata.source.mlb.handlers.BenchXml import BenchXml
from sportsdata.source.mlb.handlers.InningsAllXml import InningsAllXml
from sportsdata.source.mlb.handlers.InningHit import InningHitXml
from sportsdata.source.mlb.handlers.InningScoresXml import InningScoresXml
from sportsdata.source.mlb.handlers.BoxscoreXml import BoxscoreXml
from sportsdata.source.mlb.handlers.ScoreboardXml import ScoreboardXml
from sportsdata.source.mlb.handlers.GameXml import GameXml
from sportsdata.source.mlb.handlers.GamedaySynXml import GamedaySynXml
from sportsdata.source.mlb.handlers.GameEventsXml import GameEventsXml

class MLB:
    domain_name = 'mlb.com'

    def benchXml(self, game_id, returnXml = False):
        """
        Retrieves and optionally processes the bench.xml for a given game
        Args:
            game_id: Identifier for the game

        Returns:

        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/bench.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        x = urlopen(url)
        xml_data = x.read()

        if returnXml == True:
            return xml_data

        bench_xml = BenchXml()
        xml.sax.parseString(xml_data, bench_xml)
        return bench_xml.bench


    def benchOXml(self, game_id, returnXml = False):
        """
        Retrieves and optionally processes the benchO.xml for a given game
        (The 'official' bench xml file)

        Args:
            game_id: Identifier for the game
            returnXml:

        Returns:

        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/benchO.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)

        x = urlopen(url)
        xml_data = x.read()

        if returnXml == True:
            return xml_data

        bench_xml = BenchXml()
        xml.sax.parseString(xml_data, bench_xml)
        return bench_xml.bench

    def boxscoreXml(self, game_id, returnXml = False):
        """
        Retrieves, and optionally processes the boxscore.xml file

        Args:
            game_id: Identifier for the game
        :return:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/boxscore.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        print(url)

        x = urlopen(url)
        xml_data = x.read()

        if returnXml == True:
            return xml_data

        boxscore_xml = BoxscoreXml()
        xml.sax.parseString(xml_data,boxscore_xml)
        return boxscore_xml.boxscore

    def careerHitting(self,player_id,game_type,returnJson=False):
        """

        Args:
            player_id:
            game_type:
            returnJson:

        Returns:

        """
        url = "/json/named.sport_career_hitting.bam?league_list_id='mlb'&game_type={0}&player_id={1}"
        url = url.format(game_type, player_id)
        x = urlopen(url)
        json_data = str(x.read(), 'ISO-8859-1').encode('utf8')

        if returnJson:
            return json_data

        data = json.loads(json_data)
        return data

    def copyrightTxt(self):
        """
        Retrieves the MLBAM License governing the usage of their data
        :return: (String) Copyright Text
        """
        url = "http://gdx.mlb.com/components/copyright.txt"
        x = urlopen(url)
        copyright_text = x.read()
        return copyright_text

    def gameXml(self, game_id, returnXml = False):
        """
        Retrieves, and optionally processes the game.xml file

        Args:
            game_id: Identifier for the game
        Returns:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/game.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        print(url)

        x = urlopen(url)
        xml_data = x.read()

        if returnXml == True:
            return xml_data

        game_xml = GameXml()
        xml.sax.parseString(xml_data, game_xml)
        return game_xml.game

    def gameday_SynXml(self, game_id, returnXml = False):
        """

        :param game_id:
        :return:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/gameday_Syn.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        print(url)
        x = urlopen(url)
        xml_data = x.read()

        if returnXml == True:
            return xml_data

        gameday_syn_xml = GamedaySynXml()
        xml.sax.parseString(xml_data,gameday_syn_xml)


    def gameEventsXml(self, game_id, returnXml = False):
        """
        Retrieve, and optionally process, the game_events.xml file

        Args:
            game_id: Identifier for the game

        Returns:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/game_events.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)

        x = urlopen(url)
        xml_data = x.read()

        if returnXml == True:
            return xml_data

        game_events_xml = GameEventsXml()
        xml.sax.parseString(xml_data,game_events_xml)
        return game_events_xml.game


    def inningsAllXml(self, game_id, returnXml = False):
        """
        Retrieves, and optionally parses the inning_all.xml

        Args:
            game_id:  MLB game id
            returnXml: Controls if the xml data

        Returns:
            inning_all.xml's content or a Game object
        """

        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/inning/inning_all.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        print(url)
        x = urlopen(url)
        data = x.read()

        if returnXml == True:
            return data

        innings_all_xml = InningsAllXml()
        xml.sax.parseString(data, innings_all_xml)
        return innings_all_xml.game

    def inningHitXml(self, game_id, returnXml = False):
        """

        :param game_id:
        :return:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/inning/inning_hit.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        x = urlopen(url)
        xml_data = x.read()

        if returnXml == True:
            return xml_data

        inning_hit_xml = InningHitXml()
        xml.sax.parseString(xml_data, inning_hit_xml)
        return inning_hit_xml.hits

    def inningScoresXml(self, game_id, returnXml=False):
        """

        :param:
            game_id

        :return:
        @todo Correctly Parse this xml file
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/inning/inning_Scores.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        print(url)
        x = urlopen(url)
        xml_data = x.read()

        if returnXml:
            return xml_data

        inning_scores_xml = InningScoresXml()
        xml.sax.parseString(xml_data,inning_scores_xml)
        return inning_scores_xml.hits


    def playerInfoJson(self, player_id, returnJson=False):
        """
        Retrieves, and optionally process, the player_info.bam JSON endpoint

        Args:
            player_id:

        Returns:

        """
        url = "http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='{0}'"
        url = url.format(player_id)
        print(url)
        x = urlopen(url)
        json_data = str(x.read(),'ISO-8859-1').encode('utf8')

        if (returnJson==True):
            return json_data

        data = json.loads(json_data)
        return data

    def playerTeams(self, season=None, player_id=None):
        """

        Args:
            player_id: Player ID (Required)
            season:
        Returns:

        """
        url = "http://lookup-service-prod.mlb.com/json/named.player_teams.bam?season='{0}'&player_id='{1}'"

        url = url.format(season, player_id)

    def rawboxscoreXml(self, game_id, returnXml = False):
        """

        :param game_id:
        :return:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/rawboxscore.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        x = urlopen(url)
        data = x.read()

        if returnXml:
            return data

        boxscore_xml = BoxscoreXml()
        xml.sax.parseString(data, boxscore_xml)
        return boxscore_xml.boxscore


    def scoreboardXml(self, lookup_date, returnXml = False):
        """
        Retrieves, and optionally processes the scoreboard.xml file for a given date.
        :param:
            lookup_date

        :returns:
            Scoreboard, if returnXml == False
            (XML) string, if returnXml == True
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1:02d}/day_{2:02d}/scoreboard.xml"
        url = url.format(lookup_date.year, lookup_date.month, lookup_date.day)
        print(url)
        x = urlopen(url)
        data = x.read()

        if returnXml:
            return data

        scoreboardXml = ScoreboardXml()
        xml.sax.parseString(data, scoreboardXml)
        return scoreboardXml.scoreboard


    def searchPlayerAllJson(self,active_sw=None,name_part=None,returnJson=False):
        """

        Args:
            active_sw:
            name_part:

        Returns:

        """
        url = "http://lookup-service-prod.mlb.com/ json/named.search_player_all.bam?sport_code = 'mlb'"


        if (active_sw):
            url += "&active_sw={0}".format(active_sw)

        if (name_part):
            url += "&name_part={0}".format(name_part)

        x = urlopen(url)
        json_data = str(x.read(), 'ISO-8859-1').encode('utf8')

        if returnJson:
            return json_data

        data = json.loads(json_data)
        return data


    def sportHitting(self,player_id, game_type, season, returnJson=False):
        """

        Args:
            player_id:
            game_type:
            season:
            returnJson:

        Returns:

        """
        url = "http://lookup-service-prod.mlb.com/json/named.sport_hitting_tm.bam?league_list_id='mlb'&game_type={0}&season={1}&player_id={2}"
        url = url.format(game_type,season,player_id)
        x = urlopen(url)
        json_data = str(x.read(), 'ISO-8859-1').encode('utf8')

        if returnJson:
            return json_data

        data = json.loads(json_data)
        return data

    def sportPitching(self, player_id, game_type, season, returnJson=False):
        """
        Args:
            game_type:
            season:
            player_id
        Returns:

        """
        url = "http://lookup-service-prod.mlb.com/json/named.sport_pitching_tm.bam?league_list_id='mlb'&game_type={0}&season={1}&player_id={2}"
        url = url.format(game_type,season,player_id)
        x = urlopen(url)
        json_data = str(x.read(), 'ISO-8859-1').encode('utf8')

        if returnJson:
           return json_data

        data = json.loads(json_data)
        return data
