from sports.source.nba.nba_team import NBA_Team


class LosAngelesClippers(NBA_Team):
    """
    NBA Los Angeles Clippers Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Los Angeles Clippers"
        self.name       = "Clippers"
        self.team_id    = 1610612746
