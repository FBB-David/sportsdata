import xml.sax

class Scoreboard(xml.sax.ContentHandler):
    def __init__(self):
        self.info = None
        self.linescore = None
        self.inning_line_scores = []


    def startElement(self, name, attrs):
        if name == 'boxscore':
            self.info = dict(attrs)
        elif name == 'linescore':
            self.linescore = dict(attrs)
        elif name == 'inning_line_score':
            self.inning_line_scores.append(dict(attrs))