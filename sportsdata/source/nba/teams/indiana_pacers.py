from sportsdata.source.nba.team import NBA_Team


class IndianaPacers(NBA_Team):
    """
    NBA Atlanta Hawks Static Information

    """
    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  =   "Indiana Pacers"
        self.name       =   "Pacers"
        self.team_id    =   1610612754