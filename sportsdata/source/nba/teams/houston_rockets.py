from sportsdata.source.nba.nba_team import NBA_Team


class HoustonRockets(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Houston Rockets"
        self.name       = "Rockets"
        self.team_id    = 1610612745