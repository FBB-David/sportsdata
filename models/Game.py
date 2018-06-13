from .Bunch import Bunch
class Game(dict):
    def __init__(self, **kwargs):
        dict.__init__(self,kwargs)
        self.__dict__.update(kwargs)

        # Assigned via game.xml
        self.home_team= None
        self.away_team = None
        self.stadium = None

        # Assigned via ????
        self.innings = []