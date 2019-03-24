from sports.source.nba.nba_team import NBA_Team


class MinnesotaTimberwolves(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Minnesota Timberwolves"
        self.name       = "Timberwolves"
        self.team_id    = 1610612750
