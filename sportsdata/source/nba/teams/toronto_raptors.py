from sportsdata.source.nba.team import NBA_Team


class TorontoRaptors(NBA_Team):
    """
    NBA Atlanta Hawks Static Information

    """
    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  =   "Toronto Raptors"
        self.name       =   "Raptors"
        self.team_id    =   None