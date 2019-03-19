from sportsdata.source.nba.team import NBA_Team


class DallasMavericks(NBA_Team):
    """
    NBA Atlanta Hawks Static Information

    """
    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  =   "Dallas Mavericks"
        self.name       =   "Mavericks"
        self.team_id    =   1610612742