from sportsdata.source.nba.team import NBA_Team


class ClevelandCavaliers(NBA_Team):
    """
    NBA Atlanta Hawks Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Cleveland Cavaliers"
        self.name       = "Cavaliers"
        self.team_id    = 1610612739