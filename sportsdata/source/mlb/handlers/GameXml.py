import xml.sax
from sportsdata.models import Game
from sportsdata.models import Bunch

class GameXml(xml.sax.ContentHandler):
    def __init__(self):
        self.game = None

    def startElement(self, name, attrs):
        if name == 'game':
             self.game = Game(**attrs)
        elif name == 'team' and attrs['type'] == 'home':
            self.game.home_team = Bunch(**attrs)
        elif name == 'team' and attrs['type'] == 'away':
            self.game.away_team = Bunch(**attrs)
        elif name == 'stadium':
            self.game.stadium = Bunch(**attrs)