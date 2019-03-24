from sports.nba.nba_team import NBA_Team


class OrlandoMagic(NBA_Team):
    """
    NBA Orlando Magic Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Orlando Magic"
        self.name       = "Magic"
        self.team_id    = 1610612753
