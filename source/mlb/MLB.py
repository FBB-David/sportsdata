from urllib.request import urlopen
from .BenchXml import BenchXml
from .InningsAllXml import InningsAllXml
from .BoxscoreXml import BoxscoreXml
from .ScoreboardXml import ScoreboardXml

import xml

class MLB:
    domain_name = 'mlb.com'

    def copyrightTxt(self):
        """

        :return:
        """
        url = "http://gdx.mlb.com/components/copyright.txt"
        print(url)


    def benchXml(self, game_id, returnXml = False):
        """
        Retrieves and optionally processes the bench.xml for a given game
        Args:
            game_id:

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
        return bench_xml


    def benchOXml(self, game_id, returnXml = False):
        """
        Retrieves and optionally processes the benchO.xml for a given game
        (The 'official' bench xml file)

        Args:
            game_id:
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
        return bench_xml

    def boxscoreXml(self, game_id):
        """

        :param game_id:
        :return:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/boxscore.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        print(url)

    def gameXml(self, game_id):
        """

        :param game_id:
        :return:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/game.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        print(url)


    def gameday_SynXml(self, game_id):
        """

        :param game_id:
        :return:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/gameday_Syn.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        print(url)

    def gameEventsXml(self, game_id):
        """
        1. Retrieve the game_events.xml file
        :param game_id:
        :return:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/game_events.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)


        #return urlopen(GAME_URL.format(year, month, day, game_id,
        #                               'game_events.xml'))


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
        x = urlopen(url)
        data = x.read()

        if returnXml == True:
            return data

        innings_all_xml = InningsAllXml()
        xml.sax.parseString(data, innings_all_xml)
        return innings_all_xml.game

    def inningHitXml(self, game_id):
        """

        :param game_id:
        :return:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/inning_hit.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        print(url)


    def inningScoresXml(self, game_id):
        """

        :param:
            game_id

        :return:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/inning_Scores.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        print(url)


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