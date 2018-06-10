from urllib.request import urlopen
from .Bench import Bench
from .InningsAllXml import InningsAllXml
from .Scoreboard import Scoreboard

import xml

class MLB:
    domain_name = 'mlb.com'

    def copyrightTxt(self):
        """

        :return:
        """
        url = "http://gdx.mlb.com/components/copyright.txt"
        print(url)

    def bench(self, game_id):
        """
        1. Par
        :param game_id:
        :return:
        """
        xmlData = self.benchXml(game_id)
        benchXmlData = Bench()
        xml.sax.parseString(xmlData, benchXmlData)
        print(len(benchXmlData.homePitchers))
        print(len(benchXmlData.awayPitchers))


    def benchXml(self, game_id):
        """

        :param game_id:
        :return:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/bench.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        print(url)
        x = urlopen(url)
        data = x.read()
        return data


    def benchOXml(self, game_id):
        """

        :param game_id:
        :return:
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/benchO.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        print(url)

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
        print(url)
        x = urlopen(url)
        data = x.read()

        if returnXml:
            return data

        boxscore = Scoreboard()
        xml.sax.parseString(data, boxscore)
        return boxscore


    def scoreboardXml(self, game_id, returnXml = False):
        """
        Retrieves, and optionally processes the scoreboard.xml file for a given game.

        :param:
            game_id

        :returns:
            Scoreboard, if returnXml == False
            (XML) string, if returnXml == True
        """
        url = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/gid_{3}/scoreboard.xml"
        year, month, day, _discard = game_id.split('_', 3)
        url = url.format(year, month, day, game_id)
        x = urlopen(url)
        data = x.read()

        if returnXml:
            return data

        scoreboard = Scoreboard()
        xml.sax.parseString(data, scoreboard)
        return scoreboard