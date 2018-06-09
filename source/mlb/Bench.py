import xml.sax

class Bench(xml.sax.ContentHandler):


    def __init__(self):
        self.awayPitchers = []
        self.awayBatters  = []
        self.awayTeamID   = None
        self.homePitchers = []
        self.homeBatters  = []
        self.homeTeamID   = None
        self.isHomeOrAway = None

    def startElement(self, tag, attributes):
        if tag == "away":
            self.isHomeOrAway = tag
            self.awayTeamID   = attributes['tid']
        elif tag == 'batter' and self.isHomeOrAway == 'away':
            self.awayBatters.append(dict(attributes))
        elif tag == 'batter' and self.isHomeOrAway == 'home':
            self.homeBatters.append(dict(attributes))
        elif tag == "pitcher" and self.isHomeOrAway == 'away':
            self.awayPitchers.append(dict(attributes))
        elif tag == "pitcher" and self.isHomeOrAway == 'home':
            self.homePitchers.append(dict(attributes))
        elif tag == "home":
            self.isHomeOrAway = tag
            self.homeTeamID = attributes['tid']