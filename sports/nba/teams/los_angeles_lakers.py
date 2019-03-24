from sports.source.nba.nba_team import NBA_Team


class LosAngelesLakers(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Los Angeles Lakers"
        self.name       = "Lakers"
        self.team_id    = 1610612747