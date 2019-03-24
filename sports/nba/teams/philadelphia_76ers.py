from sports.source.nba.nba_team import NBA_Team


class Philadelphia76ers(NBA_Team):
    """
    NBA's Philadelphia 76ers Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Philadelphia 76ers"
        self.name       = "76ers"
        self.team_id    = 1610612755
