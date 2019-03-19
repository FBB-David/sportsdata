from sportsdata.source.nba.team import NBA_Team


class SacramentoKings(NBA_Team):
    """
    NBA Los Angeles Clippers Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Sacramento Kings"
        self.name       = "Kings"
        self.team_id    = None