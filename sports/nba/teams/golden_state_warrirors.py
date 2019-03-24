from sports.nba.nba_team import NBA_Team


class GoldenStateWarriors(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Golden State Warriors"
        self.name       = "Warriors"
        self.team_id    = 1610612744