from sports.source.nba.nba_team import NBA_Team


class NewYorkKnickerbockers(NBA_Team):
    """
    NBA's New York Knickerbockers Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "New York Knickerbockers"
        self.name       = "Knickerbockers"
        self.team_id    = 1610612752