from sportsdata.source.nba.team import NBA_Team


class MemphisGrizzlies(NBA_Team):
    """
    NBA Memphis Grizzlies Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Memphis Grizzlies"
        self.name       = "Grizzlies"
        self.team_id    = 1610612763
