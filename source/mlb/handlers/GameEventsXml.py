import xml.sax
from sportsdata.models.Game import Game
from sportsdata.models.AtBat import AtBat
from sportsdata.models.Bunch import Bunch

class GameEventsXml(xml.sax.ContentHandler):
    def __init__(self):
        self.game = None
        self.currentAtBat = None
        self.currentAction = None
        self.currentPitch = None

    def startElement(self, name, attrs):
        if name == 'atbat':
            if self.currentAtBat != None:
                self.game.at_bats.append(self.currentAtBat)
            self.currentAtBat = AtBat(**attrs)
        elif name == 'atBat':
            pass
        elif name == 'action':
            if self.currentAction != None:
                self.currentAtBat.actions.append(self.currentAction)
            self.currentAction = Bunch(**attrs)
        elif name == 'bottom':
            pass
        elif name == 'deck':
            pass
        elif name == 'game':
            self.game = Game(**attrs)
        elif name == 'hole':
            pass
        elif name == 'inning':
            pass
        elif name == 'pitch':
            if self.currentPitch != None:
                self.currentAtBat.pitches.append(self.currentPitch)
            self.currentPitch = Bunch(**attrs)
        elif name == 'top':
            pass
        else:
            print(name)