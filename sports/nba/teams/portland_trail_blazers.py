from sports.source.nba.nba_team import NBA_Team


class PortlandTrailBlazers(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Portland TrailBlazers"
        self.name       = "TrailBlazers"
        self.team_id    = 1610612757
