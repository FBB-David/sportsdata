from sports.source.nba.nba_team import NBA_Team


class SacramentoKings(NBA_Team):
    """
    NBA's Sacramento Kings Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Sacramento Kings"
        self.name       = "Kings"
        self.team_id    = 1610612758