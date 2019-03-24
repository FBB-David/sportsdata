from sports.nba.nba_team import NBA_Team


class BostonCeltics(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Boston Celtics"
        self.name       = "Celtics"
        self.team_id    = 1610612738