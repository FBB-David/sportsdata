from sportsdata.source.nba.nba_team import NBA_Team

class AtlantaHawks(NBA_Team):
    """
    NBA Atlanta Hawks Static Information

    """
    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  =   "Atlanta Hawks"
        self.name       =   "Hawks"
        self.team_id    =   1610612737