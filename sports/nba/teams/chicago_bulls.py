from sports.source.nba.nba_team import NBA_Team


class ChicagoBulls(NBA_Team):
    """
    NBA Atlanta Hawks Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Chicago Bulls"
        self.name       = "Bulls"
        self.team_id    = 1610612741