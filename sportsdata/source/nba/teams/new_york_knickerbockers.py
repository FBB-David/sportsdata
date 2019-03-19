from sportsdata.source.nba.team import NBA_Team


class NewYorkKnickerbockers(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "New York Knickerbockers"
        self.name       = "Suns"
        self.team_id    = None