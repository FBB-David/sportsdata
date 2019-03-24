from sports.nba.nba_team import NBA_Team


class DetroitPistons(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "DetroitPistons"
        self.name       = "Pistons"
        self.team_id    = 1610612765