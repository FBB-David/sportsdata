import xml.sax

class Game(xml.sax.ContentHandler):

    def __init__(self):
        self.currentInning = None
        self.currentAtBat  = None
        self.innings       = []


    def startElement(self, name, attrs):
        if name == 'game':
            for k, v in attrs.items():
                setattr(self, k, v)
        elif name == 'inning':
            self.currentInning = int(attrs['num'])
            pass
        elif name == 'atbat':
            self.currentAtBat = int(attrs['num'])
            pass