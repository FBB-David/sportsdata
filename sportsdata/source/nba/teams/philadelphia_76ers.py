from sportsdata.source.nba.team import NBA_Team


class Philadelphia76ers(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Philadelphia 76ers"
        self.name       = "Suns"
        self.team_id    = None
