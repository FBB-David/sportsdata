from sports.source.nba.nba_team import NBA_Team


class TorontoRaptors(NBA_Team):
    """
    NBA's Toronto Raptors Static Information

    """
    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  =   "Toronto Raptors"
        self.name       =   "Raptors"
        self.team_id    =   1610612761