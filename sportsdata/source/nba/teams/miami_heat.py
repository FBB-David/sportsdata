from sportsdata.source.nba.team import NBA_Team


class MiamiHeat(NBA_Team):
    """
    NBA Memphis Grizzlies Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Miami Heat"
        self.name       = "Heat"
        self.team_id    = 1610612748
