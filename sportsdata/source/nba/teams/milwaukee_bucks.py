from sportsdata.source.nba.nba_team import NBA_Team


class MilwaukeeBucks(NBA_Team):
    """
    NBA Memphis Grizzlies Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Milwaukee Bucks"
        self.name       = "Bucks"
        self.team_id    = 1610612749
